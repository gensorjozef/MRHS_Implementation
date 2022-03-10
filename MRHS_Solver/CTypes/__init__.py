import ctypes.util
from ctypes import *
from MRHS_Solver import MRHS, BlockMatrix
from MRHS_Solver.CTypes.CStructs import _bm, MRHS_system
import MRHS_Solver.CTypes.utils as utils
import os.path
import platform
import time
from collections.abc import Callable

dll_name: str
if (platform.system() == "Windows"):
    dll_name = "MRHS.dll"
elif (platform.system() == "Linux"):
    dll_name = "MRHS.so"
else:
    raise Exception("Unsupported operating system (Supported= Windows,Linux )")

dll_absolute_path = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + dll_name
mrhs_lib = ctypes.CDLL(dll_absolute_path)

# function prototypes
mrhs_lib.wrapped_solve_rz_file_out.argtypes = (MRHS_system, c_int, POINTER(c_longlong), POINTER(c_longlong), POINTER(c_longlong),c_int,c_char_p )
mrhs_lib.wrapped_solve_hc_file_out.argtypes = (MRHS_system, c_int, POINTER(c_longlong), POINTER(c_longlong), POINTER(c_longlong),c_int,c_char_p )
mrhs_lib.wrapped_solve_rz.argtypes = (MRHS_system, c_int, POINTER(c_longlong), POINTER(c_longlong), POINTER(c_longlong), c_int, CFUNCTYPE(c_int, c_longlong))
mrhs_lib.wrapped_solve_hc.argtypes = (MRHS_system, c_int, POINTER(c_longlong), POINTER(c_longlong), POINTER(c_longlong), c_int, CFUNCTYPE(c_int, c_longlong))


mrhs_lib.wrapped_create_mrhs_fixed.argtypes = (c_int, c_int, c_int, c_int)
mrhs_lib.wrapped_create_mrhs_fixed.restype = POINTER(MRHS_system)

mrhs_lib.wrapped_create_mrhs_variable.argtypes = (c_int, c_int, POINTER(c_int), POINTER(c_int))
mrhs_lib.wrapped_create_mrhs_variable.restype = POINTER(MRHS_system)


class SolverReport:
    def __init__(self, results: POINTER(c_longlong),
                 run_time: float,
                 xors: POINTER(c_longlong),
                 solutions_count: POINTER(c_longlong),
                 save_results: int = 0):
        self.results: list[int] = []

        save_count = 0
        if save_results < solutions_count.contents.value:
            save_count = save_results
        else:
            save_count = solutions_count.contents.value
        if save_count > 0:
            self.results = [results[i].value for i in range(save_count)]

        self.run_time: float = run_time
        self.xor_count: int = xors.contents.value
        self.found_solutions: int = solutions_count.contents.value

    def print_results(self):
        print("Found solutions: {}".format(self.found_solutions))
        print("Xors used: {}".format(self.xor_count))
        print("Runtime (s): {}".format(self.run_time))

    def get_solution(self) -> int:
        if len(self.results) <= 0:
            return None

        while True:
            for solution in self.results:
                yield solution
            return None


class CTypeMRHS:

    def __init__(self, mrhs: MRHS = None, callback = None):
        self._dll_allocated = False
        if (mrhs != None):
            self.set_py_mrhs(mrhs)
        else:
            self._py_system = None
            self._c_system = MRHS_system()
        self._call_solution_callback_prototype = CFUNCTYPE(c_int, c_longlong)
        self.call_solution_callback = None

        if callback is not None:
            self.call_solution_callback = self._call_solution_callback_prototype(callback)

    def _solution_callback(self,sol):
        print(sol)

    def set_py_mrhs(self, mrhs: MRHS):
        self._py_system = mrhs
        block_array: list[BlockMatrix] = mrhs.block_array

        num_blocks = len(block_array)
        blocks: list[_bm] = []
        rhs: list[_bm] = []

        for i in range(num_blocks):
            blocks.append(utils.convert_matrix_to_cblock(block_array[i].matrix))
            rhs.append(utils.convert_matrix_to_cblock(block_array[i].rhsMatrix.matrix))

        self._c_system: MRHS_system = MRHS_system(num_blocks,
                                                  (_bm * len(blocks))(*blocks),
                                                  (_bm * len(rhs))(*rhs)
                                                  )

    def get_py_mrhs(self) -> MRHS.MRHS:
        num_blocks: c_int = self.c_system.nblocks
        mat_blocks: _bm = self.c_system.pM
        rhs_blocks: _bm = self.c_system.pS

        mat: list[list[list[int]]] = []

        for i in range(num_blocks):
            mat_block: _bm = mat_blocks[i]
            rhs_block: _bm = rhs_blocks[i]

            mat_block_vectors = []
            for j in range(mat_block.nrows):
                ar = utils.bitfield(mat_block.rows[j])
                ar_len = len(ar)
                for k in range(mat_block.ncols - ar_len):
                    ar.insert(0, 0)
                mat_block_vectors.append(ar)

            rhs_block_vectors = []
            for j in range(rhs_block.nrows):
                ar = utils.bitfield(rhs_block.rows[j])
                ar_len = len(ar)
                for k in range(rhs_block.ncols - ar_len):
                    ar.insert(0, 0)
                rhs_block_vectors.append(ar)
            comb = []
            comb.append(mat_block_vectors)
            comb.append(rhs_block_vectors)
            mat.append(comb)
        return MRHS.MRHS(mat)

    @property
    def c_system(self) -> MRHS_system:
        return self._c_system

    def solve(self, max_t, report_solutions: int = 0, algorithm="hc", save_file: str = None) -> SolverReport:
        if algorithm == "hc":
            return self._prepare_solve(max_t, save_file, 0, report_solutions)
        elif algorithm == "rz":
            return self._prepare_solve(max_t, save_file, 1, report_solutions)
        else:
            raise Exception("Algorithm \"{}\" is not valid implementation".format(algorithm))

    def _prepare_solve(self, max_t, save_file, algorithm_id, save_results) -> SolverReport:
        maxt: c_int = c_int(max_t)

        p_count = c_longlong(0)
        pCount: POINTER(c_longlong) = pointer(p_count)  # Allocated

        p_restarts = c_longlong(0)
        pRestarts: POINTER(c_longlong) = pointer(p_restarts)  # Allocated

        p_results: POINTER(c_longlong) = (POINTER(c_longlong))()  # Null pointer

        start_time = time.time()
        if algorithm_id == 0:
            self.solve_hc(maxt, pCount, pRestarts, p_results, save_file, save_results)
        elif algorithm_id == 1:
            self.solve_rz(maxt, pCount, pRestarts, p_results, save_file, save_results)

        run_time = time.time() - start_time
        return SolverReport(p_results, run_time, pRestarts, pCount, save_results)

    def solve_rz(self, maxt, pCount, pRestarts, p_results, save_file: str = None, save_results: int = 0):
        res = 0
        if save_file is None:
            res = mrhs_lib.wrapped_solve_rz(self.c_system,
                                            maxt,
                                            pCount,
                                            pRestarts,
                                            p_results,
                                            c_int(save_results),
                                            self.call_solution_callback)
        else:
            res = mrhs_lib.wrapped_solve_rz_file_out(self.c_system,
                                                     maxt,
                                                     pCount,
                                                     pRestarts,
                                                     p_results,
                                                     c_int(save_results),
                                                     create_string_buffer(("{}".format(save_file)).encode("ASCII")))

    def solve_hc(self, maxt, pCount, pRestarts, p_results, save_file: str = None, save_results: int = 0):
        res = 0
        if save_file is None:
            res = mrhs_lib.wrapped_solve_hc(self.c_system,
                                            maxt,
                                            pCount,
                                            pRestarts,
                                            p_results,
                                            c_int(save_results),
                                            self.call_solution_callback)
        else:
            res = mrhs_lib.wrapped_solve_hc_file_out(self.c_system,
                                                     maxt,
                                                     pCount,
                                                     pRestarts,
                                                     p_results,
                                                     c_int(save_results),
                                                     create_string_buffer(("{}".format(save_file)).encode("ASCII")))

    def create_mrhs_fixed(self, nrows: int, nblocks: int, blocksize: int, rhscount: int):
        if self._dll_allocated:
            self._clear_mrhs()
        self._dll_allocated = True

        ret = mrhs_lib.wrapped_create_mrhs_fixed(c_int(nrows),
                                                 c_int(nblocks),
                                                 c_int(blocksize),
                                                 c_int(rhscount))

        self._c_system = ret.contents

    def create_mrhs_variable(self, nrows: int, nblocks: int, blocksizes: list[int], rhscounts: list[int]):
        if (self._dll_allocated):
            self._clear_mrhs()
        self._dll_allocated = True
        blocksizes_c = (c_int * nblocks)(*blocksizes[:nblocks])
        rhscounts_c = (c_int * nblocks)(*rhscounts[:nblocks])
        ret = mrhs_lib.wrapped_create_mrhs_variable(c_int(nrows),
                                                    c_int(nblocks),
                                                    blocksizes_c,
                                                    rhscounts_c)
        self._c_system = ret.contents

    def fill_mrhs_random(self):
        mrhs_lib.wrapped_fill_mrhs_random(pointer(self.c_system))

    def fill_mrhs_random_sparse(self):
        mrhs_lib.wrapped_fill_mrhs_random_sparse(pointer(self.c_system))

    def fill_mrhs_random_sparse_extra(self, density: int):
        mrhs_lib.wrapped_fill_mrhs_random_sparse_extra(pointer(self.c_system), c_int(density))

    def __del__(self):
        if (self._dll_allocated):
            self._clear_mrhs()

    def _clear_mrhs(self):
        mrhs_lib.wrapped_clear_MRHS(pointer(self.c_system))
        self._c_system = None
        self._dll_allocated = False

import ctypes.util
from ctypes import *
from MRHS_Solver import MRHS, BlockMatrix
from MRHS_Solver.CTypes.CStructs import _bm, MRHS_system
import MRHS_Solver.CTypes.utils as utils
import os.path

dll_name= "MRHS.dll"
dll_absolute_path = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + dll_name
mrhs_lib = ctypes.CDLL(dll_absolute_path)

mrhs_lib.wrapped_create_mrhs_fixed.argtypes = (c_int, c_int, c_int, c_int)
mrhs_lib.wrapped_create_mrhs_fixed.restype = POINTER(MRHS_system)
mrhs_lib.wrapped_create_mrhs_variable.argtypes = (c_int, c_int, POINTER(c_int), POINTER(c_int))
mrhs_lib.wrapped_create_mrhs_variable.restype = POINTER(MRHS_system)

class CTypeMRHS:

    def __init__(self, mrhs: MRHS = None):
        self._dll_alocated = False
        if(mrhs != None):
            self.set_py_mrhs(mrhs)
        else:
            self._py_system = None
            self._c_system = MRHS_system()

    def set_py_mrhs(self, mrhs:MRHS):
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

        mat : list[list[list[int]]] = []

        for i in range(num_blocks):
            mat_block: _bm = mat_blocks[i]
            rhs_block: _bm = rhs_blocks[i]

            mat_block_vectors = []
            for j in range(mat_block.nrows):
                ar = utils.bitfield(mat_block.rows[j])
                ar_len = len(ar)
                for k in range(mat_block.ncols - ar_len):
                    ar.insert(0,0)
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

    def solve_hc(self,max_t: int):
        maxt: c_int = c_int(max_t)
        p_count = c_longlong(0)
        pCount: POINTER(c_longlong) = pointer(p_count)
        p_restarts = c_longlong(0)
        pRestarts: POINTER(c_longlong) = pointer(p_restarts)
        res = mrhs_lib.wrapped_solve_hc(self.c_system, maxt, pCount, pRestarts)
        print(res)

    def create_mrhs_fixed(self,nrows: int, nblocks: int, blocksize: int, rhscount: int):
        if (self._dll_alocated):
            self._clear_mrhs()
        self._dll_alocated = True

        ret = mrhs_lib.wrapped_create_mrhs_fixed(c_int(nrows),
                                                 c_int(nblocks),
                                                 c_int(blocksize),
                                                 c_int(rhscount))

        self._c_system = ret.contents

    def create_mrhs_variable(self,nrows: int, nblocks: int, blocksizes: list[int], rhscounts: list[int]):
        if(self._dll_alocated):
            self._clear_mrhs()
        self._dll_alocated = True
        blocksizes_c = (c_int *nblocks)(*blocksizes[:nblocks])
        rhscounts_c = (c_int*nblocks)(*rhscounts[:nblocks])
        ret =mrhs_lib.wrapped_create_mrhs_variable(c_int(nrows),
                                                   c_int(nblocks),
                                                   blocksizes_c,
                                                   rhscounts_c)
        self._c_system = ret.contents

    def fill_mrhs_random(self):
        mrhs_lib.wrapped_fill_mrhs_random(pointer(self.c_system))

    def fill_mrhs_random_sparse(self):
        mrhs_lib.wrapped_fill_mrhs_random_sparse(pointer(self.c_system))

    def fill_mrhs_random_sparse_extra(self,density:int):
        mrhs_lib.wrapped_fill_mrhs_random_sparse_extra(pointer(self.c_system), c_int(density))

    def __del__(self):
        if(self._dll_alocated):
            self._clear_mrhs()

    def _clear_mrhs(self):
        mrhs_lib.wrapped_clear_MRHS(pointer(self.c_system))
        self._c_system = None
        self._dll_alocated = False






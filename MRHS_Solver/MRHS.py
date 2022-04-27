from MRHS_Solver.BlockMatrix import *
from MRHS_Solver.EchelonMRHS import _convert_to_echelon_mrhs
from MRHS_Solver.SolveMRHS import _find_all_solutions_recursively, _find_all_solutions_brute_force
from MRHS_Solver.FileHandler import _convert_to_file, _load_mrhs_from_file
from MRHS_Solver.Utils import _initialise_2d_matrix


class MRHS:
    """
    Class for MRHS
    """
    def __init__(self, vectors=None):
        """
        Initialize Matrix with 3D array
        :param vectors: Arrays of vectors for each block
        """
        if vectors:
            self.block_array = []
            for vector in vectors:
                bm = BlockMatrix(vector)
                self.block_array.append(bm)
            self.vector_size = len(vectors[0][0])
            self.ident_matrix = self._create_indentity_mat()

        self.methods = {'r': self._solve_recursive,
                        'bf': self._solve_brute_force}

    def init_random(self, rows, block_num, block_lens, rhs_lens):
        """
        Checks if parameters are valid. If yes, it initializes a random MRHS.
        :param rows: integer
        :param block_num: integer
        :param block_lens: list of integers
        :param rhs_lens: list of integers
        :return: None
        """
        if _check_parameters(block_num, block_lens, rhs_lens):
            self.vector_size = rows
            self.block_array = []
            for i in range(block_num):
                block_matrix_i = _initialise_2d_matrix(block_lens[i], rows)
                rhs_matrix_i = _initialise_2d_matrix(block_lens[i], rhs_lens[i])
                block_i = BlockMatrix([block_matrix_i, rhs_matrix_i])
                block_i.fill_random()
                self.block_array.append(block_i)
            self.ident_matrix = self._create_indentity_mat()

    def init_with_vectors(self, vectors):
        """
        Initializes a MRHS from vectors.
        :param vectors: 3D list
        :return: None
        """
        self.block_array = []
        for vector in vectors:
            bm = BlockMatrix(vector)
            self.block_array.append(bm)
        self.vector_size = len(vectors[0][0])
        self.ident_matrix = self._create_indentity_mat()

    def init_with_file(self, file_name):
        """
        Initializes a MRHS from a file.
        :param file_name: name of the file
        :return: None
        """
        vectors = _load_mrhs_from_file(file_name)
        self.init_with_vectors(vectors)

    def _create_indentity_mat(self):
        """
        Initializes identity matrix in MRHS.
        :return: None
        """
        i_mat = []
        for i in range(self.vector_size):
            row = []
            for j in range(self.vector_size):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)
            i_mat.append(row)
        return i_mat

    def print_mrhs(self):
        """
        Prints formated MRHS
        :return:
        """
        for row in range(self.vector_size):
            for block in self.block_array:
                block.print_row(row)
                print(' ', end='')
            print()
        mrhs_len = sum([len(i.matrix[0]) + 1 for i in self.block_array]) - 1
        print("-" * mrhs_len)
        printing = True
        rhs_id = 0
        while printing:
            printing = False
            for block in self.block_array:
                if block.try_print_rhs(rhs_id):
                    printing = True
                    print(' ', end='')
                else:
                    print(' ' * (len(block.matrix[0]) + 1), end='')
            print()
            rhs_id += 1

    def _solve_recursive(self):
        """
        Converts MRHS to echelon form and returns all solutions using a recursive function.
        :return: all solutions as a 2D list
        """
        _convert_to_echelon_mrhs(self)
        return _find_all_solutions_recursively(self)

    def _solve_brute_force(self):
        """
        Returns all solutions using brute force.
        :return: all solutions as a 2D list
        """
        return _find_all_solutions_brute_force(self)

    def solve(self, method='r'):
        """
        Solves MRHS based on method selected.
        :param method: solving method
        :return: all solutions as a 2D list
        """
        return self.methods[method]()

    def convert_to_echelon(self):
        """
        Converts MRHS to echelon form.
        :return: None
        """
        _convert_to_echelon_mrhs(self)

    def convert_to_file(self, file_name):
        """
        Writes MRHS into a file.
        :param file_name: name of the file
        :return: None
        """
        _convert_to_file(self, file_name)


def _check_parameters(block_num, block_lens, rhs_lens):
    """
    Checks in parameters for creating MRHS are valid.
    :param block_num: integer
    :param block_lens: list of integers
    :param rhs_lens: list of integers
    :return: boolean
    """
    checker = True
    if len(block_lens) != block_num:
        print(f'The number of blocks -> {block_num} is not equal to number of block lengths -> {len(block_lens)}.')
        checker = False
    if len(rhs_lens) != block_num:
        print(f'The number of blocks -> {block_num} is not equal to number of RHS numbers -> {len(rhs_lens)}.')
        checker = False
    for i, rhs in enumerate(rhs_lens):
        max_rhs_num = 2 ** block_lens[i]
        curr_rhs_len = rhs
        if curr_rhs_len > max_rhs_num:
            print(f'RHS number -> {curr_rhs_len} on position -> {i} is greater than the maximum possible number of RHS '
                  f'-> {max_rhs_num}')
            checker = False
    return checker

from MRHS_Solver.BlockMatrix import *
from MRHS_Solver.EchelonMRHS import _convert_to_echelon_mrhs
from MRHS_Solver.SolveMRHS import _find_all_solutions_recursively, _find_all_solutions_brute_force
from MRHS_Solver.Utils import bitfield
from MRHS_Solver.RHS import *
import random


class MRHS:
    """
    Class for MRHS
    """

    def __init__(self, vectors):
        """
        Initialize Matrix with 3D array
        :param vectors: Arrays of vectors for each block
        """
        self.block_array = []
        for vector in vectors:
            bm = BlockMatrix()
            bm._init_with_matrix(vector)
            self.block_array.append(bm)
        self.vector_size = len(vectors[0][0])
        self.ident_matrix = self._create_indentity_mat()

    def _fill_random(self):
        """
        Fills matrix with random values
        """
        for bm in self.block_array:
            bm.fill_random()

    def _create_indentity_mat(self):
        """
        Creates identity matrix
        :return: identity matrix (2D array)
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
        print("-" * 30)
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

    def solve_recursive(self):
        """
        Returns all solutions using a recursive function.
        :return: all solutions as a 2D list
        """
        return _find_all_solutions_recursively(self)

    def solve_brute_force(self):
        """
        Returns all solutions using brute force.
        :return: all solutions as a 2D list
        """
        return _find_all_solutions_brute_force(self)

    def convert_to_echelon(self):
        """
        Converts MRHS to echelon form.
        :return: None
        """
        _convert_to_echelon_mrhs(self)

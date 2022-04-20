from MRHS_Solver.BlockMatrix import *
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
        self.ident_matrix = self.create_indentity_mat()

    def fill_random(self):
        """
        Fills matrix with random values
        """
        for bm in self.block_array:
            bm.fill_random()

    def create_indentity_mat(self):
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


from MRHS_Solver.RHS import *
from MRHS_Solver.Utils import *


class BlockMatrix:
    """
    Class for block in MRHS
    """
    def __init__(self, matrix):
        """
        Initialzie block matrix with input matrix
        :param matrix: input matrix
        """
        self.matrix = matrix[0]
        self.rhsMatrix = RHS(matrix[1])
        self.pivots = 0

    def fill_random(self):
        """
        Fills Block matrix with random
        """
        fill_2d_matrix_random(self.matrix)
        self.rhsMatrix.fill_random()

    def print_row(self, row_id):
        """
        Prints row with id of mat
        :param row_id: row_id
        """
        for row_byte in self.matrix[row_id]:
            print(row_byte, end='')

    def try_print_rhs(self, rhs_id):
        """
        Try to print rhs
        :param rhs_id: rhsID
        """
        if rhs_id < len(self.rhsMatrix.matrix):
            self.rhsMatrix.print_row(rhs_id)
            return True
        return False

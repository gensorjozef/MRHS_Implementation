from MRHS_Solver.RHS import *


class BlockMatrix:
    """
    Class for block in MRHS
    """
    def _init_with_matrix(self, matrix):
        """
        Initialzie block matrix with input matrix
        :param matrix: input matrix
        """
        self.matrix = matrix[0]
        self.rhsMatrix = RHS()
        self.rhsMatrix.init_with_vectors(matrix[1])
        self.pivots = 0

    def __int__(self, mat):
        """
        Initialzie block matrix with input matrix
        :param mat: input matrix
        """
        self._init_with_matrix(mat)

    def fill_random(self):
        """
        Fills Block matrix with random
        """
        fill_2d_matrix_random(self.matrix)
        self.rhsMatrix.fill_random()

    def remove_block_matrix_dupes(self):
        """
        Removes block matrix dupes from RHS
        """
        for row in self.rhsMatrix.matrix:
            if self.rhsMatrix.contains_duplicate(row):
                self.rhsMatrix.remove_first_duplicate(row)

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

from MRHS_Solver.Controllers import *
from MRHS_Solver.RHS import *

class BlockMatrix:

   # def __init__(self, dim_x, dim_y, rhs, ran=False):
     #   self.matrix = initialise_2d_matrix(dim_x, dim_y)
      #  self.rhsMatrix = rhs
      #  if ran:
      #      self.matrix = fill_2d_matrix_random(self.matrix)
      #      self.remove_block_matrix_dupes()
      #  print("Created BlockMatrix")

    def initWithMatrix(self,matrix):
        self.matrix = matrix[0]
        self.rhsMatrix = RHS()
        self.rhsMatrix.initWithVectors(matrix[1])

    def __int__(self, mat):
        self.matrix = mat[0]
        self.rhsMatrix = RHS()
        self.rhsMatrix.initWithVectors(mat[1])

    def remove_block_matrix_dupes(self):
        for row in self.rhsMatrix.matrix:
            if self.rhsMatrix.contains_duplicate(row):
                self.rhsMatrix.remove_first_duplicate(row)

    def print_row(self, row_id):
        for row_byte in self.matrix[row_id]:
            print(row_byte, end='')

    def try_print_rhs(self, rhs_id):
        if rhs_id < len(self.rhsMatrix.matrix):
            self.rhsMatrix.print_row(rhs_id)
            return True
        return False
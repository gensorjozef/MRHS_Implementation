from MRHS_Solver.Controllers import *

class RHS:
    #def __init__(self, vector_len, vector_count, ran=False):
      #  self.matrix = initialise_2d_matrix(vector_len, vector_count)
      #  if ran:
      #      self.matrix = fill_2d_matrix_random(self.matrix)
      #  print("Created RHS")

    def __int__(self,vectors):
        self.matrix = vectors

    def initWithVectors(self,vectors):
        self.matrix = vectors

    def contains_duplicate(self, vec):
        count = 0

        for row in self.matrix:
            cont = True
            for col in range(len(row)):
                if row[col] != vec[col]:
                    cont = False
            if cont:
                count += 1
        if count > 1:
            return True
        return False

    def remove_first_duplicate(self, vec):
        for row in self.matrix:
            cont = True
            for col in range(len(row)):
                if row[col] != vec[col]:
                    cont = False
            if cont:
                self.matrix.remove(row)
                return

    def contains(self, vec):
        for row in self.matrix:
            cont = True
            for col in range(len(row)):
                if row[col] != vec[col]:
                    cont = False
            if cont:
                return True
        return False

    def print_row(self, row_id):
        for row_byte in self.matrix[row_id]:
            print(row_byte, end='')


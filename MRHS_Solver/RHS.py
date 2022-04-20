from MRHS_Solver.Utils import *

class RHS:
    """
    Class for RHS of BLockMatrices
    """
    def __int__(self,vectors):
        """
        Initialzie RHS with vectors
        """
        self.matrix = vectors

    def init_with_vectors(self, vectors):
        self.matrix = vectors

    def fill_random(self):
        """
        Fills random RHS
        """
        fill_2d_matrix_random(self.matrix)

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
        """
        Prints row of RHS
        :param row_id: rowID
        """
        for row_byte in self.matrix[row_id]:
            print(row_byte, end='')


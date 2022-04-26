from MRHS_Solver.Utils import _generate_random_vectors
import random


class RHS:
    """
    Class for RHS of BlockMatrix
    """

    def __init__(self, vectors):
        """
        Initialzie RHS with vectors
        """
        self.matrix = vectors

    def fill_random(self):
        """
        Fills random RHS
        """
        vectors = _generate_random_vectors(len(self.matrix[0]), len(self.matrix))
        random.shuffle(vectors)
        self.matrix = vectors

    def print_row(self, row_id):
        """
        Prints row of RHS
        :param row_id: rowID
        """
        for row_byte in self.matrix[row_id]:
            print(row_byte, end='')

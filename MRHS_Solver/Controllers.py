
class Controllers:

    def __init__(self):
        pass

    def fill_2d_matrix_random(mat):
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                mat[row][col] = get_random_byte()

        return mat

    def initialise_2d_matrix(dimX, dimY):
        m = [[0] * dimX for i in range(dimY)]
        return m

    def bitfield(n):
        return [int(digit) for digit in bin(n)[2:]]

def get_random_byte():
    return random.randint(0, 1)
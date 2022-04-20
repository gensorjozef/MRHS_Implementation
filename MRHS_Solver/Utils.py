import random


def fill_2d_matrix_random(mat):
    """
    Fills matrix with random values
    :param mat: matrix
    :return: matrix
    """
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            mat[row][col] = get_random_bit()

    return mat


def initialise_2d_matrix(dimX, dimY):
    """
    Initialise 2D matrix
    :param dimX: dimension X
    :param dimY: dimension Y
    :return: Initialised matrix
    """
    m = [[0] * dimX for i in range(dimY)]
    return m


def bitfield(n):
    """
    Converts number to list of bits
    :param n: number
    :return: list of bits
    """
    return [int(digit) for digit in bin(n)[2:]]


def get_random_bit():
    """
    Gets random byte
    :return: random bit (0/1)
    """
    return random.randint(0, 1)

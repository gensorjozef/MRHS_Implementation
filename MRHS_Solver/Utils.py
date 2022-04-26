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


def generate_random_vectors(vec_len: int, num_of_vecs: int) -> list[list[int]]:
    """
    Creates num_of_vecs random vectors with length of vec_len.
    :param num_of_vecs: number of vectors we want (must be lower than 2^vec_len)
    :param vec_len: length of vectors
    :return: vectors as a 2D list
    """
    vectors = []
    vec_num = 2 ** vec_len
    set_of_vecs = set()

    while len(set_of_vecs) < num_of_vecs:
        set_of_vecs.add(random.randint(0, vec_num - 1))

    for i in set_of_vecs:
        vec = [int(digit) for digit in bin(i)[2:]]
        for j in range(vec_len - len(vec)):
            vec.insert(0, 0)
        vectors.append(vec)

    return vectors

import numpy as np
from MRHS_Solver import MRHS as ms
from MRHS_Solver import LoadFile as lf


def extract_matrix_from_mrhs(mrhs):
    mat = []
    for i in range(mrhs.vector_size):
        row = []
        for j in range(len(mrhs.block_array)):
            for k in range(len(mrhs.block_array[j].matrix[0])):
                row.append(mrhs.block_array[j].matrix[i][k])
        mat.append(row)
    return np.matrix(mat)


def update_mrhs_matrix(mrhs, mat):
    tmp_mat = mat.tolist()
    for i in range(mrhs.vector_size):
        col = 0
        for j in range(len(mrhs.block_array)):
            for k in range(len(mrhs.block_array[j].matrix[0])):
                mrhs.block_array[j].matrix[i][k] = tmp_mat[i][col]
                col += 1


def gf2elim(M):
    m, n = M.shape

    i = 0
    j = 0

    while i < m and j < n:
        # find value and index of largest element in remainder of column j
        k = np.argmax(M[i:, j]) + i

        # swap rows
        # M[[k, i]] = M[[i, k]] this doesn't work with numba
        temp = np.copy(M[k])
        M[k] = M[i]
        M[i] = temp

        aijn = M[i, j:]

        col = np.copy(M[:, j])  # make a copy otherwise M will be directly affected

        col[i] = 0  # avoid xoring pivot row with itself

        flip = np.outer(col, aijn)

        M[:, j:] = M[:, j:] ^ flip

        i += 1
        j += 1

    return M


def gauss_elim_mrhs(mrhs):
    mat = extract_matrix_from_mrhs(mrhs)
    gf2elim(mat)
    update_mrhs_matrix(mrhs, mat)


mat = lf.LoadFile("D:\škola\TP1\MRHS_Implementation\input.txt").get_final_matrix()
mrhs = ms.MRHS(mat)
mrhs.print_mrhs()

gauss_elim_mrhs(mrhs)

mrhs.print_mrhs()

from MRHS_Solver.CTypes import CTypeMRHS


def extract_matrix_from_mrhs(mrhs):
    mat = []
    for i in range(mrhs.vector_size):
        row = []
        for j in range(len(mrhs.block_array)):
            for k in range(len(mrhs.block_array[j].matrix[0])):
                row.append(mrhs.block_array[j].matrix[i][k])
        mat.append(row)
    return mat


def update_mrhs_matrix(mrhs, mat):
    for i in range(mrhs.vector_size):
        col = 0
        for j in range(len(mrhs.block_array)):
            for k in range(len(mrhs.block_array[j].matrix[0])):
                mrhs.block_array[j].matrix[i][k] = mat[i][col]
                col += 1


def xor(row1, row2):
    row_out = []
    for i in range(len(row1)):
        row_out.append(row1[i] ^ row2[i])
    return row_out


def swap_rows(row1, row2, mat):
    tmp = mat[row1]
    mat[row1] = mat[row2]
    mat[row2] = tmp


def create_pivots(mat):
    rows = len(mat)
    cols = len(mat[0])
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1:
                row_i = mat[i]
                for k in range(i + 1, rows):
                    if mat[k][j] == 1:
                        mat[k] = xor(mat[k], row_i)
                break


def find_index_of_pivot(mat, col):
    rows = len(mat)
    for i in range(rows):
        if mat[i][col] == 1:
            return i


def is_pivot(row, col, mat):
    if mat[row][col] == 0:
        return False
    for j in range(col):
        if mat[row][j] == 1:
            return False
    return True


def sort_rows(mat):
    rows = len(mat)
    i = 0
    j = 0
    while True:
        if i >= rows - 1:
            break
        i_piv = find_index_of_pivot(mat, j)
        if not is_pivot(i_piv, j, mat):
            j += 1
            continue
        if i != i_piv:
            swap_rows(i, i_piv, mat)
        j += 1
        i += 1


def sub_rows(mat):
    rows = len(mat)
    cols = len(mat[0])
    i = 1
    for j in range(1, cols):
        if not is_pivot(i, j, mat):
            j += 1
            continue
        for k in range(i):
            if mat[k][j] == 1:
                mat[k] = xor(mat[i], mat[k])
        i += 1
        if i >= rows:
            break


def gauss_elim(mat):
    create_pivots(mat)
    sort_rows(mat)
    sub_rows(mat)


# # test code
# cmrhs = CTypeMRHS()
# cmrhs.create_mrhs_fixed(6, 4, 4, 4)
# cmrhs.fill_mrhs_random_sparse_extra(2)
# mrhs = cmrhs.get_py_mrhs()
# mrhs.print_mrhs()
#
# matrix = extract_matrix_from_mrhs(mrhs)
# gauss_elim(matrix)
# update_mrhs_matrix(mrhs, matrix)
# mrhs.print_mrhs()

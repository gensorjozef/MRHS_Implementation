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


def extract_block_form_mrhs(mrhs, block_num):
    return mrhs.block_array[block_num].matrix


def update_mrhs_block(mrhs, block_num, block):
    mrhs.block_array[block_num].matrix = block


def extract_rhs_from_mrhs(mrhs, rhs_num):
    return mrhs.block_array[rhs_num].rhsMatrix.matrix


def update_mrhs_rhs(mrhs, rhs_num, rhs):
    mrhs.block_array[rhs_num].rhsMatrix.matrix = rhs


def xor_rows(row1, row2):
    row_out = []
    for i in range(len(row1)):
        row_out.append(row1[i] ^ row2[i])
    return row_out


def swap_rows(row_index1, row_index2, mat):
    tmp = mat[row_index1]
    mat[row_index1] = mat[row_index2]
    mat[row_index2] = tmp


def get_col(mat, col_index):
    column = []
    for i in range(len(mat)):
        column.append(mat[i][col_index])
    return column


def instert_col(mat, col_index, col):
    for i in range(len(mat)):
        mat[i][col_index] = col[i]


def swap_cols(col_index1, col_ndex2, mat):
    column1 = get_col(mat, col_index1)
    column2 = get_col(mat, col_ndex2)
    instert_col(mat, col_index1, column2)
    instert_col(mat, col_ndex2, column1)


def create_pivots(mat):
    rows = len(mat)
    cols = len(mat[0])
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1:
                row_i = mat[i]
                for k in range(i + 1, rows):
                    if mat[k][j] == 1:
                        mat[k] = xor_rows(mat[k], row_i)
                break


def find_row_index_of_pivot(mat, col_index):
    rows = len(mat)
    for i in range(rows):
        if mat[i][col_index] == 1:
            return i


def find_col_index_of_pivot(mat, row_index):
    cols = len(mat[0])
    for j in range(cols):
        if mat[row_index][j] == 1:
            return j
    return -1


def is_pivot_row(row_index, col_index, mat):
    if mat[row_index][col_index] == 0:
        return False
    for j in range(col_index):
        if mat[row_index][j] == 1:
            return False
    return True


def is_pivot_col(row_index, col_index, mat):
    if mat[row_index][col_index] == 0:
        return False
    for i in range(row_index):
        if mat[i][col_index] == 1:
            return False
    return True


def sort_rows(mat):
    rows = len(mat)
    i = 0
    j = 0
    while True:
        if i >= rows - 1:
            break
        i_piv = find_row_index_of_pivot(mat, j)
        if not is_pivot_row(i_piv, j, mat):
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
        if not is_pivot_row(i, j, mat):
            j += 1
            continue
        for k in range(i):
            if mat[k][j] == 1:
                mat[k] = xor_rows(mat[i], mat[k])
        i += 1
        if i >= rows:
            break


def gauss_elim(mat):
    create_pivots(mat)
    sort_rows(mat)
    sub_rows(mat)


def swap_cols_blocks_rhss(mrhs):
    last_row_index = 0
    for i in range(len(mrhs.block_array)):
        if last_row_index >= mrhs.vector_size:
            break
        block_i = extract_block_form_mrhs(mrhs, i)
        rhs_i = extract_rhs_from_mrhs(mrhs, i)
        for j in range(len(block_i[0])):
            if block_i[last_row_index][j] != 1:
                new_col_index = find_col_index_of_pivot(block_i, last_row_index)
                if new_col_index == -1:
                    break
                swap_cols(j, new_col_index, block_i)
                swap_cols(j, new_col_index, rhs_i)
            last_row_index += 1
            if last_row_index >= mrhs.vector_size:
                break
        update_mrhs_block(mrhs, i, block_i)
        update_mrhs_rhs(mrhs, i, rhs_i)


def gauss_elim_mrhs(mrhs):
    matrix = extract_matrix_from_mrhs(mrhs)
    gauss_elim(matrix)
    update_mrhs_matrix(mrhs, matrix)
    swap_cols_blocks_rhss(mrhs)


# test code
cmrhs = CTypeMRHS()
cmrhs.create_mrhs_fixed(6, 4, 4, 4)
cmrhs.fill_mrhs_random_sparse_extra(2)
mrhs = cmrhs.get_py_mrhs()
mrhs.print_mrhs()
gauss_elim_mrhs(mrhs)
mrhs.print_mrhs()

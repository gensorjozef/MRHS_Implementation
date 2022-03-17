from MRHS_Solver.CTypes import CTypeMRHS


def create_indentity_mat(mrhs):
    i_mat = []
    for i in range(mrhs.vector_size):
        row = []
        for j in range(mrhs.vector_size):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        i_mat.append(row)
    return i_mat


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


def swap_rows(row_id1, row_id2, mat):
    tmp = mat[row_id1]
    mat[row_id1] = mat[row_id2]
    mat[row_id2] = tmp


def get_col(mat, col_id):
    column = []
    for i in range(len(mat)):
        column.append(mat[i][col_id])
    return column


def instert_col(mat, col_id, col):
    for i in range(len(mat)):
        mat[i][col_id] = col[i]


def swap_cols(col_id1, col_id2, mat):
    column1 = get_col(mat, col_id1)
    column2 = get_col(mat, col_id2)
    instert_col(mat, col_id1, column2)
    instert_col(mat, col_id2, column1)


def xor_cols(col_id1, col_id2, mat):
    column1 = get_col(mat, col_id1)
    column2 = get_col(mat, col_id2)
    column_fin = []
    for i in range(len(column1)):
        column_fin.append(column1[i] ^ column2[i])
    instert_col(mat, col_id2, column_fin)


def find_row_id_of_pivot(mat, col_index):
    rows = len(mat)
    for i in range(rows):
        if mat[i][col_index] == 1:
            return i
    return -1


def find_col_id_of_pivot(mat, row_index):
    cols = len(mat[0])
    for j in range(cols):
        if mat[row_index][j] == 1:
            return j
    return -1


def is_pivot_row(row_id, col_id, mat):
    if mat[row_id][col_id] == 0:
        return False
    for j in range(col_id):
        if mat[row_id][j] == 1:
            return False
    return True


def is_pivot_col(row_id, col_id, mat):
    if mat[row_id][col_id] == 0:
        return False
    for i in range(row_id):
        if mat[i][col_id] == 1:
            return False
    return True


def create_pivots(mat):
    rows = len(mat)
    cols = len(mat[0])
    for i in range(rows):
        for j in range(cols):
            if is_pivot_row(i, j, mat):
                row_i = mat[i]
                for k in range(rows):
                    if mat[k][j] == 1 and k != i:
                        mat[k] = xor_rows(mat[k], row_i)
                break


def sort_rows(mat):
    rows = len(mat)
    i = 0
    j = 0
    while True:
        if i >= rows - 1:
            break
        i_piv = find_row_id_of_pivot(mat, j)
        if i_piv == -1:
            i += 1
            continue
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


def row_elim(mat):
    create_pivots(mat)
    sort_rows(mat)
    sub_rows(mat)


def swap_cols_blocks_rhss(mrhs):
    last_row_id = 0
    for i in range(len(mrhs.block_array)):
        if last_row_id >= mrhs.vector_size:
            break
        block_i = extract_block_form_mrhs(mrhs, i)
        rhs_i = extract_rhs_from_mrhs(mrhs, i)
        for j in range(len(block_i[0])):
            if block_i[last_row_id][j] != 1:
                new_col_id = find_col_id_of_pivot(block_i, last_row_id)
                if new_col_id == -1:
                    break
                swap_cols(j, new_col_id, block_i)
                swap_cols(j, new_col_id, rhs_i)
            last_row_id += 1
            if last_row_id >= mrhs.vector_size:
                break
        update_mrhs_block(mrhs, i, block_i)
        update_mrhs_rhs(mrhs, i, rhs_i)


def xor_cols_blocks_rhss(mrhs):
    last_row_id = 0
    for i in range(len(mrhs.block_array)):
        if last_row_id >= mrhs.vector_size:
            break
        block_i = extract_block_form_mrhs(mrhs, i)
        rhs_i = extract_rhs_from_mrhs(mrhs, i)
        for j in range(len(block_i[0])):
            if is_pivot_col(last_row_id, j, block_i):
                for k in range(j + 1, len(block_i[0])):
                    if block_i[last_row_id][k] == 1:
                        xor_cols(j, k, block_i)
                        xor_cols(j, k, rhs_i)
            last_row_id += 1
            if last_row_id >= mrhs.vector_size:
                break
        update_mrhs_block(mrhs, i, block_i)
        update_mrhs_rhs(mrhs, i, rhs_i)


def gauss_elim_mrhs(mrhs):
    # id_matrix = create_indentity_mat(mrhs) TODO
    matrix = extract_matrix_from_mrhs(mrhs)
    row_elim(matrix)
    update_mrhs_matrix(mrhs, matrix)
    swap_cols_blocks_rhss(mrhs)
    xor_cols_blocks_rhss(mrhs)


def print_mat(mat):
    for r in mat:
        print(*r)
    print()


# # test code
# cmrhs = CTypeMRHS()
# cmrhs.create_mrhs_variable(8, 4, [6, 4, 4, 4], [4, 1, 1, 7])
# cmrhs.fill_mrhs_random_sparse_extra(10)
#
# mrhs = cmrhs.get_py_mrhs()
# mrhs.print_mrhs()
#
# gauss_elim_mrhs(mrhs)
# mrhs.print_mrhs()
#
# print_mat(create_indentity_mat(mrhs))

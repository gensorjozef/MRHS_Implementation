def extract_matrix_from_mrhs(mrhs):
    """
    Extracts the matrix from MRHS object and returns it as a 2D array.
    :param mrhs: instance of class MRHS
    :return: matrix as a 2D array
    """
    mat = []
    for i in range(mrhs.vector_size):
        row = []
        for j in range(len(mrhs.block_array)):
            for k in range(len(mrhs.block_array[j].matrix[0])):
                row.append(mrhs.block_array[j].matrix[i][k])
        mat.append(row)
    return mat


def update_mrhs_matrix(mrhs, mat):
    """
    Overwrites the matrix in MRHS object.
    :param mrhs: instance of class MRHS
    :param mat: matrix as a 2D array
    :return: None
    """
    for i in range(mrhs.vector_size):
        col = 0
        for j in range(len(mrhs.block_array)):
            for k in range(len(mrhs.block_array[j].matrix[0])):
                mrhs.block_array[j].matrix[i][k] = mat[i][col]
                col += 1


def extract_block_form_mrhs(mrhs, block_num):
    """
    Returns a block with index block_num from MRHS object as a 2D array.
    :param mrhs: instance of class MRHS
    :param block_num: index of a block
    :return: block as a 2D array
    """
    return mrhs.block_array[block_num].matrix


def update_mrhs_block(mrhs, block_num, block):
    """
    Overwrites a block with index block_num in MRHS object.
    :param mrhs: instance of class MRHS
    :param block_num: index of a block
    :param block: block as a 2D array
    :return: None
    """
    mrhs.block_array[block_num].matrix = block


def extract_rhs_from_mrhs(mrhs, rhs_num):
    """
    Returns a RHS with index rhs_num from MRHS object as a 2D array.
    :param mrhs: instance of class MRHS
    :param rhs_num: index of a RHS
    :return: RHS as a 2D array
    """
    return mrhs.block_array[rhs_num].rhsMatrix.matrix


def update_mrhs_rhs(mrhs, rhs_num, rhs):
    """
    Overwrites a RHS with index rhs_num in MRHS object.
    :param mrhs: instance of class MRHS
    :param rhs_num: index of a RHS
    :param rhs: RHS as a 2D array
    :return: None
    """
    mrhs.block_array[rhs_num].rhsMatrix.matrix = rhs


def xor_rows(row1, row2):
    """
    Returns array which is a product of xoring arrays row1 and row2.
    :param row1: array
    :param row2: array
    :return: array
    """
    row_out = []
    for i in range(len(row1)):
        row_out.append(row1[i] ^ row2[i])
    return row_out


def swap_rows(row_id1, row_id2, mat):
    """
    Swaps two rows with indexes row_id1 and row_id2 in matrix mat.
    :param row_id1: index of first row
    :param row_id2: index of second row
    :param mat: matrix as a 2D array
    :return: None
    """
    tmp = mat[row_id1]
    mat[row_id1] = mat[row_id2]
    mat[row_id2] = tmp


def get_col(mat, col_id):
    """
    Rerturns a column with index col_id from matrix mat.
    :param mat: matrix as a 2D array
    :param col_id: index of a column
    :return: column as an array
    """
    column = []
    for i in range(len(mat)):
        column.append(mat[i][col_id])
    return column


def instert_col(mat, col_id, col):
    """
    Overwrites a column with index col_id.
    :param mat: matrix as a 2D array
    :param col_id: index of a column
    :param col: column
    :return: None
    """
    for i in range(len(mat)):
        mat[i][col_id] = col[i]


def swap_cols(col_id1, col_id2, mat):
    """
    Swaps two columns with indexes col_id1 and col_id2 in matrix mat.
    :param col_id1: index of first column
    :param col_id2: index of second column
    :param mat: matrix as a 2D array
    :return: None
    """
    column1 = get_col(mat, col_id1)
    column2 = get_col(mat, col_id2)
    instert_col(mat, col_id1, column2)
    instert_col(mat, col_id2, column1)


def xor_cols(col_id1, col_id2, mat):
    """
    Creates a product of xoring columns with indexes col_id1 and col_id2 and overwrites column with index col_id2 with
    this product.
    :param col_id1: index of first column
    :param col_id2: index of second column
    :param mat: matrix as a 2D array
    :return: None
    """
    column1 = get_col(mat, col_id1)
    column2 = get_col(mat, col_id2)
    column_fin = []
    for i in range(len(column1)):
        column_fin.append(column1[i] ^ column2[i])
    instert_col(mat, col_id2, column_fin)


def find_row_id_of_pivot(mat, col_index):
    """
    Returns an index of a row with a pivot if there is a pivot in column with index col_index. If there is no pivot in
    this column function returns -1.
    :param mat: matrix as a 2D array
    :param col_index: index of a column
    :return: index or -1
    """
    rows = len(mat)
    for i in range(rows):
        if mat[i][col_index] == 1:
            return i
    return -1


def find_col_id_of_pivot(mat, row_index):
    """
    Returns an index of a column with a pivot if there is a pivot in row with index row_index. If there is no pivot in
    this row function returns -1.
    :param mat: matrix as a 2D array
    :param row_index: index of a row
    :return: index or -1
    """
    cols = len(mat[0])
    for j in range(cols):
        if mat[row_index][j] == 1:
            return j
    return -1


def is_pivot_row(row_id, col_id, mat):
    """
    Checks if there are any occurences of 1 in a row with index row_id before column with index col_id.
    Returns True if an element mat[row_it][col_ide] is a pivot. Returns False otherwise.
    :param row_id: index of a row
    :param col_id: index of a column
    :param mat: matrix as a 2D array
    :return: boolean
    """
    if mat[row_id][col_id] == 0:
        return False
    for j in range(col_id):
        if mat[row_id][j] == 1:
            return False
    return True


def is_pivot_col(row_id, col_id, mat):
    """
    Checks if there are any occurences of 1 in a column with index col_id before row with index row_id.
    Returns True if an element mat[row_it][col_ide] is a pivot. Returns False otherwise.
    :param row_id: index of a row
    :param col_id: index of a column
    :param mat: matrix as a 2D array
    :return: boolean
    """
    if mat[row_id][col_id] == 0:
        return False
    for i in range(row_id):
        if mat[i][col_id] == 1:
            return False
    return True


def create_pivots(mat, i_mat):
    """
    Xors rows in mat and i_mat until every row in mat contains a pivot.
    :param mat: matrix as a 2D array
    :param i_mat: identity matrix as a 2D array
    :return: None
    """
    rows = len(mat)
    cols = len(mat[0])
    for i in range(rows):
        for j in range(cols):
            if is_pivot_row(i, j, mat):
                row_i = mat[i]
                i_row_i = i_mat[i]
                for k in range(rows):
                    if mat[k][j] == 1 and k != i:
                        mat[k] = xor_rows(mat[k], row_i)
                        i_mat[k] = xor_rows(i_mat[k], i_row_i)
                break


def sort_rows(mat, i_mat):
    """
    Swaps rows in mat and i_mat until pivots in mat are sorted in a descending order.
    :param mat: matrix as a 2D array
    :param i_mat: identity matrix as a 2D array
    :return: None
    """
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
            swap_rows(i, i_piv, i_mat)
        j += 1
        i += 1


def sub_rows(mat, i_mat):
    """
    Xors rows in mat and i_mat until there are only zeros above pivots in mat.
    :param mat: matrix as a 2D array
    :param i_mat: identity matrix as a 2D array
    :return: None
    """
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
                i_mat[k] = xor_rows(i_mat[i], i_mat[k])
        i += 1
        if i >= rows:
            break


def row_elim(mat, i_mat):
    """
    Runs all of the row functions on mat and i_mat.
    :param mat: matrix as a 2D array
    :param i_mat: identity matrix as a 2D array
    :return: None
    """
    create_pivots(mat, i_mat)
    sort_rows(mat, i_mat)
    sub_rows(mat, i_mat)


def swap_cols_blocks_rhss(mrhs):
    """
    Swaps columns in every block and its' corresponding RHS until pivots in them are in pure descending order.
    :param mrhs: instance of MRHS
    :return: None
    """
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
    """
    Xors columns in every block and its' corresponding RHS until there are only zeros after pivots.
    :param mrhs: instance of MRHS
    :return: None
    """
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
    """
    Finall function that puts MRHS into an echelon form.
    :param mrhs: instance of MRHS
    :return: None
    """
    matrix = extract_matrix_from_mrhs(mrhs)
    row_elim(matrix, mrhs.ident_matrix)
    update_mrhs_matrix(mrhs, matrix)
    swap_cols_blocks_rhss(mrhs)
    xor_cols_blocks_rhss(mrhs)


def print_mat(mat):
    """
    Helping function for printing matrix
    :param mat: matrix as a 2D array
    :return: None
    """
    for r in mat:
        print(*r)
    print()

def write_mrhs_to_file(mrhs, file_name):
    """
    Writes MRHS into a file.
    :param mrhs: instance of class MRHS
    :param file_name: name of a file
    :return: None
    """
    rowsNumber = mrhs.vector_size
    blocksNumber = len(mrhs.block_array)
    rows = []
    blockMatrix = []
    rhsMatrices = []

    for block in mrhs.block_array:
        rhs = len(block.rhsMatrix.matrix)
        col_number = len(block.matrix[0])
        rows.append([col_number, rhs])
        rhsMatrices.append(block.rhsMatrix.matrix)

    for row_id in range(rowsNumber):
        row_array = []
        for block in mrhs.block_array:
            row_array.append(block.matrix[row_id])
        blockMatrix.append(row_array)

    file = open(file_name, 'w')
    file.write(str(rowsNumber) + '\n')
    file.write(str(blocksNumber) + '\n')

    for row in rows:
        file.write(str(row[0]) + ' ' + str(row[1]) + '\n')

    for row_array in blockMatrix:
        file.write('[{0}]'.format(str(row_array).replace('[', ' ').replace(']', '').replace(',', '')[2:]) + '\n')

    for rhs_matrix in rhsMatrices:
        for rhs_row in rhs_matrix:
            file.write(str(rhs_row).replace(',', '') + '\n')
        file.write('\n')

    file.close()

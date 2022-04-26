from MRHS_Solver import MRHS


def load_file_matrix(file_name : str) -> list[list[list[int]]] :
    """
    Load normalized matrix format for MRHS
    :param file_name: file name
    :return: vectors
    """
    f = open(file_name, 'r')
    s = f.read().replace("[", "").replace("]", "").split()
    f.close()
    n = int(s[0])
    m = int(s[1])
    l = []
    k = []
    index = 2
    for i in range(m):
        l.append(int(s[index]))
        index += 1
        k.append(int(s[index]))
        index += 1

    mat = []

    for i in range(m):
        block_num = l[i]
        rhs_num = k[i]
        block = [[[0] * block_num for x in range(n)], [[0] * block_num for x in range(rhs_num)]]
        mat.append(block)

    for i in range(n):
        for j in range(m):
            nums = s[index]
            index += 1
            for h, number in enumerate(nums):
                mat[j][0][i][h] = int(number)

    for i in range(m):
        for j in range(k[i]):
            nums = s[index]
            index += 1
            for h, number in enumerate(nums):
                mat[i][1][j][h] = int(number)

    return mat


def _convert_to_file(mrhs: MRHS, file_name: str) -> None:
    """
    Writes MRHS into a file.
    :param mrhs: instance of class MRHS
    :param file_name: name of a file
    :return: None
    """
    file = open(file_name, 'w')

    file.write(str(mrhs.vector_size) + '\n')
    file.write(str(len(mrhs.block_array)) + '\n')

    for block in mrhs.block_array:
        file.write(str(len(block.matrix[0])) + ' ' + str(len(block.rhsMatrix.matrix)) + '\n')

    file.write('\n')

    for i in range(mrhs.vector_size):
        file.write('[')
        for j, block in enumerate(mrhs.block_array):
            if j == len(mrhs.block_array) - 1:
                file.write(str(block.matrix[i]).replace('[', '').replace(']', '').
                           replace(' ', '').replace(',', '') + ']\n')
            else:
                file.write(str(block.matrix[i]).replace('[', '').replace(']', '').
                           replace(' ', '').replace(',', '') + ' ')

    for block in mrhs.block_array:
        file.write('\n')
        for row in block.rhsMatrix.matrix:
            file.write(str(row).replace(',', '').replace(' ', '') + '\n')

    file.close()

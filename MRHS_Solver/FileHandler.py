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

def _load_mrhs_from_file(file_name: str) -> list[list[list[int]]]:
    file = open(file_name, 'r')
    fo = file.read().splitlines()
    file.close()

    # init phase
    init_nums = []
    init_tmp = 0
    next_line = fo[init_tmp]
    while next_line.strip() != '':
        if next_line[0] == '[':
            break
        init_nums.extend(next_line.split())
        init_tmp += 1
        next_line = fo[init_tmp]

    # rhs_nums = [int(init_nums[i + 1]) for i in range(2, len(init_nums[2:]) + 1, 2)]
    # block_nums = [int(init_nums[i]) for i in range(2, len(init_nums[2:]) + 1, 2)]

    # prepare blocks
    rows = int(init_nums[0])
    blocks_qty = int(init_nums[1])
    block_array = []
    for i in range(blocks_qty):
        block = [[], []]
        block_array.append(block)

    # fill blocks
    mat_iter = 0
    while mat_iter < rows:
        if next_line.strip() != '':
            mat_row = next_line.replace('[', '').replace(']', '').split()
            for i, block_row in enumerate(mat_row):
                block_row_arr = [int(x) for x in block_row]
                block_array[i][0].append(block_row_arr)
            mat_iter += 1
        init_tmp += 1
        next_line = fo[init_tmp]

    # fill rhs
    rhs_iter = 0
    while rhs_iter < blocks_qty:
        if next_line.strip() != '':
            while next_line.strip() != '':
                rhs_row = next_line.replace('[', '').replace(']', '')
                rhs_row_arr = [int(x) for x in rhs_row]
                block_array[rhs_iter][1].append(rhs_row_arr)
                init_tmp += 1
                if init_tmp >= len(fo):
                    break
                next_line = fo[init_tmp]
            rhs_iter += 1
        init_tmp += 1
        if init_tmp >= len(fo):
            break
        next_line = fo[init_tmp]

    return block_array


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

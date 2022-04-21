from scanf import scanf

def load_file_matrix(file_name):
    f = open(file_name,'r')
    s = f.read().replace("[","").replace("]","").split()
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
        block = [[[0]*block_num for x in range(n)], [[0]*block_num for x in range(rhs_num)]]
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


def load_file(file_name):
    """
    Returns 2D array where index corresponds to one block that contains two nested fields => block line, solutions
    :param file_name: name of the file
    :return: 2D array
    """
    file_name = file_name
    fileObj = open(file_name, "r")
    words = fileObj.read().splitlines()
    fileObj.close()
    rowsNumber = int(words[0])
    blocksNumber = int(words[1])
    matrix, blocksAnswersLen = get_matrix(blocksNumber, words, rowsNumber)
    rhs = get_rhs(blocksNumber, rowsNumber, blocksAnswersLen, words)
    final_matrix = get_final_matrix(blocksNumber, matrix, rhs)
    return final_matrix

def get_matrix(blocksNumber, words, rowsNumber):
    """
    Internal function to load matrix
    :param blocksNumber:  number of blocks
    :param words: lines from matrix
    :param rowsNumber: number of rows
    :return: 2D array, 2D array
    """
    blocksLen, blocksAnswersLen = [], []
    for i in range(blocksNumber):
        blockRaw = words[i + 2]
        blockInfo = blockRaw.split(' ')
        blockLen = blockInfo[0]
        blockAnswers = blockInfo[1]
        blocksLen.append(blockLen)
        blocksAnswersLen.append(blockAnswers)
    matrix = []
    for i in range(rowsNumber):
        rowRaw = words[2 + blocksNumber + i]
        rowRaw = rowRaw[1:len(rowRaw) - 1]  # odstrani []
        rowBlocks = rowRaw.split('  ')
        rows = []
        for rowBlock in rowBlocks:
            cols = []
            for col in rowBlock:
                if col != ' ':
                    cols.append(int(col))
            rows.append(cols)
        matrix.append(rows)
    return matrix, blocksAnswersLen


def get_rhs(blocksNumber, rowsNumber, blocksAnswersLen, words):
    """
    Internal function to load solutions
    :param blocksNumber:  number of blocks
    :param words: lines from matrix
    :param rowsNumber: number of rows
    :param blocksAnswersLen: length of answer
    :return: 2D array
    """
    sum = 2 + blocksNumber + rowsNumber
    rhs = []
    for i in range(blocksNumber):
        number = int(blocksAnswersLen[i])
        rows = []
        for j in range(number):
            rowRaw = words[sum + j]
            row = rowRaw[1:len(rowRaw) - 1]
            cols = []
            for col in row:
                if col != ' ':
                    cols.append(int(col))
            rows.append(cols)

        rhs.append(rows)
        sum += number + 1
    return rhs


def get_final_matrix(blocksNumber, matrix, rhs):
    """
    Retuns rows and solutions corresponding to block
    :param blocksNumber:  number of blocks
    :param matrix: array of left side matrix
    :param rhs: array of solutions
    :return: 2D array
    """
    final_matrix, block, block_main, block_rhs = [], [], [], []
    for i in range(blocksNumber):
        for row_main in matrix:
            block_main.append(row_main[i])
        for row_rhs in rhs[i]:
            block_rhs.append(row_rhs)
        block.append(block_main)
        block.append(block_rhs)
        final_matrix.append(block)
        block, block_main, block_rhs = [], [], []
    return final_matrix

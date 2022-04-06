def append_vectors(vec1, vec2):
    """
    Appends vectors vec1 and vec2 in left to right order.
    :param vec1: array
    :param vec2: array
    :return: array
    """
    final_vec = []
    final_vec.extend(vec1)
    final_vec.extend(vec2)
    return final_vec


def generate_vectors(vec_len):
    """
    Generates all posible vectors with length of vec_len. Returns these vectors.
    :param vec_len: length of vectors
    :return: array of arrays
    """
    vec_num = 2 ** vec_len
    vectors = []
    for i in range(vec_num):
        p_sol = [int(digit) for digit in bin(i)[2:]]
        for j in range(vec_len - len(p_sol)):
            p_sol.insert(0, 0)
        vectors.append(p_sol)
    return vectors


def brute_force_solution(mrhs):
    """
    Finds solutions to MRHS via brute forcing all possible vectors. Returns these solutions.
    :param mrhs: instance of MRHS
    :return: array of arrays
    """
    test_vecs = generate_vectors(mrhs.vector_size)
    all_solutions = []
    for vec in test_vecs:
        result_vec = []
        for block in mrhs.block_array:
            part_result = []
            for i in range(len(block.matrix[0])):
                num = 0
                for j in range(len(vec)):
                    out = block.matrix[j][i] * vec[j]
                    num += out
                part_result.append(num % 2)

            if block.rhsMatrix.matrix.count(part_result) > 0:
                result_vec.extend(part_result)
                if len(result_vec) == sum(len(b.matrix[0]) for b in mrhs.block_array):
                    all_solutions.append(vec)
            else:
                break

    print(f'Solutions found by brute force: {all_solutions}')
    return all_solutions


def get_partial_rhs(rhs_len, block_num, mrhs):
    """
    Returns array with parts of RHS with length of rhs_len.
    :param rhs_len: length of RHS
    :param block_num: id of block in MRHS
    :param mrhs: instance of MRHS
    :return: array of arrays
    """
    vectors = []
    for rhs in mrhs.block_array[block_num].rhsMatrix.matrix:
        tmp_vec = rhs[:rhs_len]
        if vectors.count(tmp_vec) == 0:
            vectors.append(tmp_vec)
    return vectors


def multiply_vec_block(vec, block_num, mrhs):
    """
    Multiplyes vector with block. Returns the product of this multiplication.
    :param vec: array
    :param block_num: id of block in MRHS
    :param mrhs: instance of MRHS
    :return: array
    """
    result_vec = []
    for j in range(len(mrhs.block_array[block_num].matrix[0])):
        num = 0
        for i in range(len(vec)):
            out = mrhs.block_array[block_num].matrix[i][j] * vec[i]
            num += out
        result_vec.append(num % 2)
    return result_vec


def is_solution(vec, block_num, mrhs):
    """
    Returns True if vec is in RHS. Returns False otherwise.
    :param vec: array
    :param block_num: id of block in MRHS
    :param mrhs: instance of MRHS
    :return: boolean
    """
    if mrhs.block_array[block_num].rhsMatrix.matrix.count(vec) > 0:
        return True
    return False


def multiply_vec_block_v2(rhs_len, vec, block_num, mrhs):
    """
    Multiplies vector with block from offset of rhs_len. Returns the product of this multiplication.
    :param rhs_len: length of RHS
    :param vec: array
    :param block_num: id of block in MRHS
    :param mrhs: instance of MRHS
    :return: array
    """
    result_vec = []
    for j in range(rhs_len, len(mrhs.block_array[block_num].matrix[0])):
        num = 0
        for i in range(len(vec)):
            out = mrhs.block_array[block_num].matrix[i][j] * vec[i]
            num += out
        result_vec.append(num % 2)
    return result_vec


def is_solution_v2(partial_rhs, vec, block_num, mrhs):
    """
    Connects partial_rhs and vec and checks if that product is in RHS.
    :param partial_rhs: array
    :param vec: array
    :param block_num: id of block in MRHS
    :param mrhs: instance of MRHS
    :return: boolean
    """
    connected = append_vectors(partial_rhs, vec)
    if mrhs.block_array[block_num].rhsMatrix.matrix.count(connected) > 0:
        return True
    return False


def get_vectors(part_sol, block_num, mrhs):
    """
    If block contains only pivots, function appends all RHS to part_sol and returns these new vectors. If there is at
    least one pivot, function appends part of all RHS with length of number of pivots to part_sol and multipies these
    products with part of block. If parts of RHS appended with the products of thier multiplication are in RHS, function
    returns these new vectors. Otherwise, when there are no pivots in block, function multipies part_sol with block and
    checks if that product is in RHS. If it is then it returns these vectors.
    :param part_sol: array
    :param block_num: id of block in MRHS
    :param mrhs: instance of MRHS
    :return: array of arrays
    """
    offset = len(mrhs.block_array[block_num].matrix[0]) - mrhs.block_array[block_num].pivots
    rhs_len = len(mrhs.block_array[block_num].matrix[0]) - offset
    final_vectors = []

    if offset == 0:
        for rhs in mrhs.block_array[block_num].rhsMatrix.matrix:
            tmp_sol = part_sol.copy()
            tmp_sol.extend(rhs)
            final_vectors.append(tmp_sol)

    elif rhs_len > 0:
        vectors = get_partial_rhs(rhs_len, block_num, mrhs)
        for partial_rhs in vectors:
            tmp_sol = part_sol.copy()
            tmp_sol.extend(partial_rhs)

            result_vec = multiply_vec_block_v2(rhs_len, tmp_sol, block_num, mrhs)
            if is_solution_v2(partial_rhs, result_vec, block_num, mrhs) and final_vectors.count(tmp_sol) == 0:
                final_vectors.append(tmp_sol)

    else:
        result_vec = multiply_vec_block(part_sol, block_num, mrhs)
        if is_solution(result_vec, block_num, mrhs):
            final_vectors.append(part_sol)

    return final_vectors


def recursive_solution(part_sol, final_sol, block_num, mrhs, all_sols):
    """
    Firstly, function creates new possible partial solutions. If there no possible partial solutions, functions returns
    None. Otherwise, for each of these new partial solutions, function updates partial solution to this new value and
    calls itself with incremented block id. If the block number is at its maximum function updates final solution,
    appends it to all solutions.
    :param part_sol: array
    :param final_sol: array
    :param block_num: id of block in MRHS
    :param mrhs: instance of MRHS
    :param all_sols: array of arrays
    :return: array or None
    """
    vectors = get_vectors(part_sol, block_num, mrhs)
    if len(vectors) == 0:
        return None
    else:
        for v in vectors:
            if block_num == len(mrhs.block_array) - 1:
                final_sol = v
                all_sols.append(final_sol)
            else:
                part_sol = v
                final_sol = recursive_solution(part_sol, final_sol, block_num + 1, mrhs, all_sols)

        return final_sol


def find_solution_final(mrhs):
    """
    Initializes inputs for function recursive_solution and calls it.
    :param mrhs: instance of MRHS
    :return: array of all possible solutions for MRHS
    """
    part_sol = []
    final_sol = []
    all_sols = []
    recursive_solution(part_sol, final_sol, 0, mrhs, all_sols)
    print(f'Solutions found recursively: {all_sols}')
    return all_sols


def transform_solution(solution, mrhs):
    """
    Tranforms solution by multiplying it with identity matrix from MRHS to get solution for original MRHS.
    :param solution: array as a solution to MRHS
    :param mrhs: instance of MRHS
    :return: array as a transformed solution to MRHS
    """
    transformed = []
    for i in range(len(solution)):
        num = 0
        for j in range(len(solution)):
            out = solution[j] * mrhs.ident_matrix[j][i]
            num += out
        transformed.append(num % 2)
    print(f'Tranformed solution: {transformed}')
    return transformed


def check_solution(solution, mrhs):
    """
    Returns True if solution is valid, returns False otherwise.
    :param solution: array as a solution to MRHS
    :param mrhs: instance of MRHS
    :return: boolean
    """
    for block in mrhs.block_array:
        part_res = []
        for i in range(len(block.matrix[0])):
            num = 0
            for j in range(len(solution)):
                out = solution[j] * block.matrix[j][i]
                num += out
            part_res.append(num % 2)
        if block.rhsMatrix.matrix.count(part_res) < 1:
            print(f'Solution "{solution}" is not valid.')
            return False

    print(f'Solution "{solution}" is valid.')
    return True

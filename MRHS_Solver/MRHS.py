import random


class MRHS:

    #def __init__(self, vector_size):
      #  self.block_array = []
      #  self.vector_size = vector_size
    def __init__(self, vectors):
        self.block_array =[]
        for vector in vectors:
            bm = BlockMatrix()
            bm.initWithMatrix(vector)
            self.block_array.append(bm)
        self.vector_size = len(vectors[0][0])

    def initWithMatrix(self, vectors):
        for vector in vectors:
            bm = BlockMatrix(0,0,[])
            bm.initWithMatrix(vector)
            self.block_array = bm
        self.vector_size = len(vectors[0][0])


    def generate_random_block_array(self, block_count, block_size, rhs_fill, seed=1891499):
        random.seed(seed)
        rhs_count = int((block_size ** 2) * rhs_fill)
        for n in range(block_count):
            rhs = RHS(block_size, rhs_count, ran=True)
            self.block_array.append(BlockMatrix(block_size, self.vector_size, rhs, ran=True))

    def generate_random_block_array(self,blocks, rhs_fill, seed=1891499): #blocks = [4,1,2,3]
        random.seed(seed)
        for block in blocks:
            rhs_count = int((block ** 2) * rhs_fill)
            rhs = RHS(block, rhs_count, ran=True)
            self.block_array.append(BlockMatrix(block, self.vector_size, rhs, ran=True))

    def print_mrhs(self):
        for row in range(self.vector_size):
            for block in self.block_array:
                block.print_row(row)
                print(' ', end='')
            print()
        print("-" * 30)
        printing = True
        rhs_id = 0
        while printing:

            printing = False
            for block in self.block_array:
                if block.try_print_rhs(rhs_id):
                    printing = True
                    print(' ', end='')
                else:
                    print(' ' * (len(block.matrix[0]) + 1), end='')
            print()
            rhs_id += 1

    def find_solution(self):
        num = 2 ** self.vector_size
        print("Testing {} vectors...".format(num))
        for i in range(num):
            if self.solve_with_vector(i):
                vec = bitfield(i)
                for j in range(self.vector_size - len(vec)):
                    vec.insert(0, 0)
                yield vec
        yield None

    #1


    def find_all_solutions(self):
        solutions = []
        num = 2 ** self.vector_size
        print("Testing {} vectors...".format(num))
        for i in range(num):
            if self.solve_with_vector(i):
                vec = bitfield(i)
                for j in range(self.vector_size - len(vec)):
                    vec.insert(0, 0)
                solutions.append(vec)

        return solutions

    def solve_with_vector(self, vector):
        vector_array = bitfield(vector)
        vector_array_fin = vector_array.copy()
        for i in range(self.vector_size - len(vector_array)):
            vector_array_fin.insert(0, 0)
        # print(vector_array_fin)
        for block in self.block_array:
            block_res = []
            for row_index in range(len(block.matrix[0])):
                num = 0
                for col_index in range(self.vector_size):
                    out = block.matrix[col_index][row_index] * vector_array_fin[col_index]
                    num += out
                block_res.append(num % 2)
            # print(block_res)
            if not block.rhsMatrix.contains(block_res):
                return False

        return True


class BlockMatrix:

   # def __init__(self, dim_x, dim_y, rhs, ran=False):
     #   self.matrix = initialise_2d_matrix(dim_x, dim_y)
      #  self.rhsMatrix = rhs
      #  if ran:
      #      self.matrix = fill_2d_matrix_random(self.matrix)
      #      self.remove_block_matrix_dupes()
      #  print("Created BlockMatrix")

    def initWithMatrix(self,matrix):
        self.matrix = matrix[0]
        self.rhsMatrix = RHS()
        self.rhsMatrix.initWithVectors(matrix[1])

    def __int__(self, mat):
        self.matrix = mat[0]
        self.rhsMatrix = RHS()
        self.rhsMatrix.initWithVectors(mat[1])

    def remove_block_matrix_dupes(self):
        for row in self.rhsMatrix.matrix:
            if self.rhsMatrix.contains_duplicate(row):
                self.rhsMatrix.remove_first_duplicate(row)

    def print_row(self, row_id):
        for row_byte in self.matrix[row_id]:
            print(row_byte, end='')

    def try_print_rhs(self, rhs_id):
        if rhs_id < len(self.rhsMatrix.matrix):
            self.rhsMatrix.print_row(rhs_id)
            return True
        return False


class RHS:
    #def __init__(self, vector_len, vector_count, ran=False):
      #  self.matrix = initialise_2d_matrix(vector_len, vector_count)
      #  if ran:
      #      self.matrix = fill_2d_matrix_random(self.matrix)
      #  print("Created RHS")

    def __int__(self,vectors):
        self.matrix = vectors

    def initWithVectors(self,vectors):
        self.matrix = vectors

    def contains_duplicate(self, vec):
        count = 0

        for row in self.matrix:
            cont = True
            for col in range(len(row)):
                if row[col] != vec[col]:
                    cont = False
            if cont:
                count += 1
        if count > 1:
            return True
        return False

    def remove_first_duplicate(self, vec):
        for row in self.matrix:
            cont = True
            for col in range(len(row)):
                if row[col] != vec[col]:
                    cont = False
            if cont:
                self.matrix.remove(row)
                return

    def contains(self, vec):
        for row in self.matrix:
            cont = True
            for col in range(len(row)):
                if row[col] != vec[col]:
                    cont = False
            if cont:
                return True
        return False

    def print_row(self, row_id):
        for row_byte in self.matrix[row_id]:
            print(row_byte, end='')


def fill_2d_matrix_random(mat):
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            mat[row][col] = get_random_byte()
    return mat


def initialise_2d_matrix(dimX, dimY):
    m = [[0] * dimX for i in range(dimY)]
    return m


def get_random_byte():
    return random.randint(0, 1)


def bitfield(n):
    return [int(digit) for digit in bin(n)[2:]]

class LoadFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_from_file(self):
        print(self.file_name)

        fileObj = open(self.file_name, "r")  # opens the file in read mode
        words = fileObj.read().splitlines()  # puts the file into an array
        fileObj.close()
        rowsNumber = int(words[0])
        blocksNumber = int(words[1])
        blocksLen = []
        blocksAnswersLen = []
        for i in range(blocksNumber):
            blockRaw = words[i+1]
            blockInfo = blockRaw.split(' ')
            blockLen = blockInfo[0]
            blockAnswers = blockInfo[1]
            blocksLen.append(blockLen)
            blocksAnswersLen.append(blockAnswers)
        matrix = [[] for j in range(blocksNumber)]
        for i in range(rowsNumber):
            rowRaw = words[1+blocksNumber+i]
            rowRaw = rowRaw[1:len(rowRaw)-1] # odstrani []
            rowBlocks = rowRaw.split('  ')

            for rowBlock in rowBlocks:
                cols = []
                for col in rowBlock:
                    cols.append(col)
                matrix.append(cols)
        print(matrix)


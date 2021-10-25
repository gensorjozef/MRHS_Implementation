import random

class MRHS:

    def __init__(self,vector_size):
        self.block_array = []
        self.vector_size = vector_size

    def GenerateRandomBlockArray(self, block_count, block_size, rhs_fill, seed=1891499):
        random.seed(seed)
        rhs_count = int((block_size ** 2) * rhs_fill)
        for n in range(block_count):
            rhs = RHS(block_size, rhs_count, ran=True)
            self.block_array.append(BlockMatrix(block_size, self.vector_size, rhs, ran=True))

    def PrintMRHS(self):
        for row in range(self.vector_size):
            for block in self.block_array:
                block.PrintRow(row)
                print(' ', end='')
            print()
        print("-" * 30)
        printing = True
        rhs_id = 0
        while (printing):

            printing = False
            for block in self.block_array:
                if (block.TryPrintRhs(rhs_id)):
                    printing = True
                    print(' ', end='')
            print()
            rhs_id += 1

    def FindAllSolutions(self):
        solutions = []
        num = 2 ** self.vector_size
        print("Testing {} vectors...".format(num))
        for i in range(num):
            if self.SolveWithVector(i):
                vec = bitfield(i)
                for j in range(self.vector_size - len(vec)):
                    vec.insert(0, 0)
                solutions.append(vec)

        return solutions


    def SolveWithVector(self, vector):
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

    def __init__(self,dim_x,dim_y,rhs,ran=False):
        self.matrix = Initialise2DMatrix(dim_x,dim_y)
        self.rhsMatrix = rhs
        if (ran):
            self.matrix = Fill2DMatrixRandom(self.matrix)
            self.removeDupes()
        print("Created BlockMatrix")

    def removeDupes(self):
        for row in self.rhsMatrix.matrix:
            if(self.rhsMatrix.containsDuplicate(row)):
                self.rhsMatrix.removeFirstDuplicate(row)
    def PrintRow(self,row_id):
        for row_byte in self.matrix[row_id]:
            print(row_byte, end='')

    def TryPrintRhs(self,rhs_id):
            if(rhs_id < len(self.rhsMatrix.matrix)):
                self.rhsMatrix.PrintRow(rhs_id)
                return True
            return False


class RHS:
    def __init__(self,vector_len,vector_count, ran=False):
        self.matrix = Initialise2DMatrix(vector_len,vector_count)
        if(ran):
            self.matrix = Fill2DMatrixRandom(self.matrix)
        print("Created RHS")

    def containsDuplicate(self, vec):
        count = 0

        for row in self.matrix:
            cont = True
            for col in range(len(row)):
                if (row[col] != vec[col]):
                    cont = False
            if (cont):
                count += 1
        if (count > 1):
            return True
        return False

    def removeFirstDuplicate(self, vec):
        for row in self.matrix:
            cont = True
            for col in range(len(row)):
                if (row[col] != vec[col]):
                    cont = False
            if (cont):
                self.matrix.remove(row)
                return

    def contains(self, vec):
        for row in self.matrix:
            cont = True
            for col in range(len(row)):
                if (row[col] != vec[col]):
                    cont = False
            if (cont):
                return True
        return False

    def PrintRow(self,row_id):
        for row_byte in self.matrix[row_id]:
            print(row_byte, end='')

def Fill2DMatrixRandom(mat):
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            mat[row][col] = GetRandomByte()
    return mat

def Initialise2DMatrix(dimX,dimY):
    m =[[0] * dimX for i in range(dimY)]
    return m

def GetRandomByte():
    return random.randint(0,1)

def bitfield(n):
    return [int(digit) for digit in bin(n)[2:]]

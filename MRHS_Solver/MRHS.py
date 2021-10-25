import random

class MRHS:

    def __init__(self,vector_size):
        self.block_array = []
        self.vector_size = vector_size


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

    def __init__(self,dim_x,dim_y,rhs):
        self.matrix = Initialise2DMatrix(dim_x,dim_y)
        self.rhsMatrix = rhs


        print("Created BlockMatrix")

    def removeDupes(self):
        for row in self.rhsMatrix.matrix:
            if(self.rhsMatrix.containsDuplicate(row)):
                self.rhsMatrix.removeFirstDuplicate(row)
    def PrintRow(self,row_id):
        for row_byte in self.matrix[row_id]:
            print(row_byte,end='')

 def TryPrintRhs(self,rhs_id):
        if(rhs_id < len(self.rhsMatrix.matrix)):
            self.rhsMatrix.PrintRow(rhs_id)
            return True
        return False


class RHS:
    def __init__(self,vector_len,vector_count):
        self.matrix = Initialise2DMatrix(vector_len,vector_count)

        print("Created RHS")

    def PrintRow(self,row_id):
        for row_byte in self.matrix[row_id]:
            print(row_byte,end='')

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

import random

class MRHS:

    def __init__(self,vector_size):
        self.block_array = []
        self.vector_size = vector_size



class BlockMatrix:

    def __init__(self,dim_x,dim_y,rhs):
        self.matrix = Initialise2DMatrix(dim_x,dim_y)
        self.rhsMatrix = rhs


        print("Created BlockMatrix")

    def PrintRow(self,row_id):
        for row_byte in self.matrix[row_id]:
            print(row_byte,end='')




class RHS:
    def __init__(self,vector_len,vector_count):
        self.matrix = Initialise2DMatrix(vector_len,vector_count)

        print("Created RHS")

    def PrintRow(self,row_id):
        for row_byte in self.matrix[row_id]:
            print(row_byte,end='')


def Initialise2DMatrix(dimX,dimY):
    m =[[0] * dimX for i in range(dimY)]
    return m


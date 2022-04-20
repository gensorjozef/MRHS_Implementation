from MRHS_Solver.BlockMatrix import *
from MRHS_Solver.Controllers import bitfield
from MRHS_Solver.RHS import *
import random


class MRHS:

    # def __init__(self, vector_size):
    #  self.block_array = []
    #  self.vector_size = vector_size
    def __init__(self, vectors):
        self.block_array = []
        for vector in vectors:
            bm = BlockMatrix()
            bm.initWithMatrix(vector)
            self.block_array.append(bm)
        self.vector_size = len(vectors[0][0])
        self.ident_matrix = self.create_indentity_mat()

    def initWithMatrix(self, vectors):
        for vector in vectors:
            bm = BlockMatrix(0, 0, [])
            bm.initWithMatrix(vector)
            self.block_array = bm
        self.vector_size = len(vectors[0][0])

    def create_indentity_mat(self):
        i_mat = []
        for i in range(self.vector_size):
            row = []
            for j in range(self.vector_size):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)
            i_mat.append(row)
        return i_mat

    def generate_random_block_array(self, block_count: int, block_size, rhs_fill, seed=1891499):
        random.seed(seed)
        rhs_count = int((block_size ** 2) * rhs_fill)
        for n in range(block_count):
            rhs = RHS(block_size, rhs_count, ran=True)
            self.block_array.append(BlockMatrix(block_size, self.vector_size, rhs, ran=True))

    def generate_random_block_array(self, blocks, rhs_fill, seed=1891499):  # blocks = [4,1,2,3]
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

    # 1

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

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from MRHS_Solver import MRHS as ms

if __name__ == '__main__':

    mat = ms.LoadFile("input.txt").get_final_matrix()
    mrhs = ms.MRHS(mat)
    mrhs.print_mrhs()

    # print(generator.__next__())
    # print(mrhs.find_all_solutions())
    for i in mrhs.find_solution():
        print(i)
    # print(mrhs.SolveWithVector(solution))


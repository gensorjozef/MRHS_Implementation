# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import ctypes

from MRHS_Solver import MRHS as ms
from MRHS_Solver import LoadFile as lf
from MRHS_Solver.EchelonMRHS import create_echelon_mrhs
from MRHS_Solver.SolveMRHS import find_all_solutions_recursively, find_all_solutions_brute_force


def print_solution(sol):
    print(sol)
    return 0

if __name__ == '__main__':

    mat = lf.load_file("input.txt")
    mrhs = ms.MRHS(mat)
    mrhs.print_mrhs()
    create_echelon_mrhs(mrhs)
    sols = find_all_solutions_recursively(mrhs)
    print(sols)






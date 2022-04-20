# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import ctypes

from MRHS_Solver import MRHS as ms
from MRHS_Solver import LoadFile as lf
from MRHS_Solver import CreateFile as cf
from MRHS_Solver.CTypes.CTypeMRHS import CTypeMRHS
from MRHS_Solver.EchelonMRHS import create_echelon_mrhs
from MRHS_Solver.SolveMRHS import find_all_solutions_recursively, find_all_solutions_brute_force
from time import time
from MRHS_Solver.CTypes.SolverReport import SolverReport

from time import sleep

def print_solution(sol):
    print(sol)
    return 0

if __name__ == '__main__':

    mat = lf.LoadFile("input.txt").get_final_matrix()
    mrhs = ms.MRHS(mat)

    cmrhs = CTypeMRHS(mrhs=mrhs, callback=print_solution)
    # cmrhs.get_py_mrhs().print_mrhs()
    #
    # cmrhs.create_mrhs_fixed(6, 4, 4, 4)
    # cmrhs.fill_mrhs_random()
    # cmrhs.get_py_mrhs().print_mrhs()
    #
    # cmrhs.create_mrhs_variable(6, 4, [2, 2, 2, 3], [1, 1, 1, 2])
    # cmrhs.fill_mrhs_random()
    # cmrhs.get_py_mrhs().print_mrhs()
    #
    # cmrhs.create_mrhs_variable(6, 4, [2, 2, 2, 3], [1, 1, 1, 2])
    # cmrhs.fill_mrhs_random_sparse()
    # cmrhs.get_py_mrhs().print_mrhs()

    cmrhs.create_mrhs_fixed(12, 6, 3, 4)
    cmrhs.fill_mrhs_random()

    mrhs = cmrhs.get_py_mrhs()
    mrhs.print_mrhs()

    report = cmrhs.solve(10_000, algorithm="rz", save_file="results.txt", report_solutions=0)
    report.print_results()
    for i in report.get_solution():
        print(i)
    mrhs = cmrhs.get_py_mrhs()


    current_time = time()
    create_echelon_mrhs(mrhs)
    sols = find_all_solutions_brute_force(mrhs)
    print(sols)
    file = open("resultspy.txt","w")

    file.close()
    end_time = time()
    print(end_time-current_time)
    file = cf.CreateFile(mrhs)
    file.create_file('output.txt')





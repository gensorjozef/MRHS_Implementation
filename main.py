# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import ctypes

from MRHS_Solver import MRHS as ms
from MRHS_Solver import LoadFile as lf
from MRHS_Solver import CreateFile as cf
from MRHS_Solver.CTypes import CTypeMRHS,SolverReport
import MRHS_Solver.GaussElimination as gs
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

    cmrhs.create_mrhs_fixed(6, 2, 3, 4)
    cmrhs.fill_mrhs_random_sparse_extra(2)
    report = cmrhs.solve(5000)
    report.print_results()
    mrhs = cmrhs.get_py_mrhs()

    mrhs.print_mrhs()

    file = cf.CreateFile(mrhs)
    file.create_file('output.txt')





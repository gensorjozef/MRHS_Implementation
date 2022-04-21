from MRHS_Solver import MRHS as ms
from MRHS_Solver import LoadFile as lf
from MRHS_Solver.EchelonMRHS import create_echelon_mrhs
from MRHS_Solver.SolveMRHS import find_all_solutions_recursively, find_all_solutions_brute_force
from MRHS_Solver.CTypes.CTypeMRHS import CTypeMRHS


if __name__ == '__main__':
    mat = lf.load_file_scanf("test_mrhs.txt")
    mrhs = ms.MRHS(mat)
    mrhs.print_mrhs()








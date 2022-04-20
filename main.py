from MRHS_Solver import MRHS as ms
from MRHS_Solver import LoadFile as lf
from MRHS_Solver.EchelonMRHS import create_echelon_mrhs
from MRHS_Solver.SolveMRHS import find_all_solutions_recursively, find_all_solutions_brute_force
from MRHS_Solver.CTypes.CTypeMRHS import CTypeMRHS


if __name__ == '__main__':
    mat = lf.load_file("input.txt")

    vectors = [
        [
            [[1, 0, 1], [1, 1, 1]],
            [[0, 1, 1], [1, 0, 0]]
        ],
        [
            [[1, 0], [1, 1]],
            [[0, 0], [0, 1]]
            ]
    ]

    mrhs = ms.MRHS(vectors)
    #mrhs.fill_random()
    #mrhs = ms.MRHS(mat)
    mrhs.print_mrhs()
    create_echelon_mrhs(mrhs)
    sols = find_all_solutions_recursively(mrhs)
    print(sols)






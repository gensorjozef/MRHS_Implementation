# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from MRHS_Solver import MRHS as ms

if __name__ == '__main__':
    mrhs = ms.MRHS(8)
    mrhs.GenerateRandomBlockArray(5,3,0.9,511555)
    mrhs.PrintMRHS()
    solutions = mrhs.FindAllSolutions()
    print(solutions)
    #print(mrhs.SolveWithVector(solution))



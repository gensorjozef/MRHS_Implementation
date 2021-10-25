from MRHS_Solver import MRHS as ms

if __name__ == '__main__':
    mrhs = ms.MRHS(7)
    mrhs.GenerateRandomBlockArray(4,2,0.5,True)
    mrhs.PrintMRHS()
    results = mrhs.FindAllSolutions()
    print(len(results))
    print(results)
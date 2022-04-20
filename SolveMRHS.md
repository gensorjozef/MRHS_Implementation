[MRHS_Solver](README.md#MRHS_Solver)

# Collection of functions: **SolveMRHS**

## Functions:

- [```find_all_solutions_brute_force(mrhs: MRHS) -> list[list[int]]```](#find-all-solutions-by-brute-force)
- [```find_all_solutions_recursively(echelon_mrhs: MRHS) -> list[list[int]]```](#find-all-solutions-recursively)

### Find all solutions by brute force
 ```find_all_solutions_brute_force(mrhs: MRHS) -> list[list[int]]```:
- Description
  - Function that finds solutions to MRHS via brute forcing all possible vectors.
- Parameters:
  - **mrhs** : python representation of MRHS
- Return:
  - ```list[list[int]```: list of solutions to MRHS

---

### Find all solutions recursively
 ```find_all_solutions_recursively(echelon_mrhs: MRHS) -> list[list[int]]:```
- Description
  - Function that finds all solutions to echelonized MRHS using recursive function and transforms them using identity 
  - matrix from MRHS.
- Parameters:
  - **mrhs** : python representation of MRHS
- Return:
  - ```list[list[int]```: list of solutions to MRHS
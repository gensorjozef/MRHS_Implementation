[MRHS_Solver](README.md#MRHS_Solver)

# Class: **MRHS**

## Methods:

- [```print_mrhs(self)```](#print-mrhs) 
- [```convert_to_echelon(self)```](#convert-to-echelon-form)
- [```solve_brute_force(self)```](#solve-with-brute-force)
- [```solve_recursive(self)```](#solve-recursively)

### Print MRHS
 ```print_mrhs(self)```:
- Description
  - Function that prints formated MRHS.

---

### Convert to echelon form
 ```convert_to_echelon(self)```:
- Description
  - Function that puts MRHS into an echelon form.

---

### Solve with brute force
 ```solve_brute_force(self)```
- Description
  - Function that finds solutions to MRHS via brute forcing all possible vectors.
- Return:
  - ***list[list[int]]***: list of solutions to MRHS

---

### Solve recursively
 ```solve_recursive(self)```
 - Description
  - Function that finds all solutions to echelonized MRHS using recursive function and transforms them using identity 
  - matrix from MRHS.
- Return:
  - ***list[list[int]]***: list of solutions to MRHS
# MRHS solver implementation
We are a group of developers engaged in the development of MRHS equations and its distribution. In this project, we want to expand the libraries that deal with this issue with our research.

## Usage 





### Function collections

---

#### MRHS_Solver

- [**EchelonMRHS**](EchelonMRHS.md)
  - Collection of functions for creating echelon form of MRHS

- [**SolveMRHS**](SolveMRHS.md)
  - Collection of functions for solving MRHS

- [**CreateFile**](CreateFile.md)
  - Collection of functions for writing MRHS into a text file

- [**LoadFIle**](LoadFIle.md)
  - Functions to handle input file and transform it to MRHS form

---

#### MRHS_Solver.CTypes

- [**CTypeMRHS**](CTypeMRHS.md) 
  - Wrapper class for C interactions

- [**SolverReport**](SolverReport.md)
  - Solver report class for C implementation 
  
- [*Structs*](CStructs.md)


#### Examples

##### Load MRHS from file

```python
mat = LoadFile.load_file("input.txt")
mrhs = MRHS_Solver.MRHS(mat)
mrhs.print_mrhs()
```

##### Create MRHS and fill it with random

```python
vectors = [
  [
  [[1,0,1],[1,1,1]],
  [[0,1,1],[1,0,0]]
  ],
  [1,0],[1,1]]
mrhs = MRHS_Solver.MRHS(vectors)
mrhs.fill_random()
```

##### Create Ctype MRHS and fill it with random
```python
cmrhs = CTypeMRHS()
cmrhs.create_mrhs_fixed(12, 6, 3, 4)
cmrhs.fill_mrhs_random()
mrhs = cmrhs.get_py_mrhs()
```
##### Solve MRHS using python with echelon reduction

```python
create_echelon_mrhs(mrhs)
sols = find_all_solutions_recursively(mrhs)
```

##### Generate MRHS and solve using C version

```python
cmrhs = MRHS_Solver.CTypes.CTypeMRHS()

cmrhs.create_mrhs_fixed(12, 6, 3, 4)
cmrhs.fill_mrhs_random()

#Use algorithms : 'rz' or 'hc'
report = cmrhs.solve(10_000, algorithm="rz", save_file="results.txt", report_solutions=0)
#Prints solving results
report.print_results()
```

        


# MRHS solver implementation
We are a group of developers engaged in the development of MRHS equations and its distribution. In this project, we want to expand the libraries that deal with this issue with our research.

## Usage 





### Function collections

---

#### MRHS_Solver
- [**MRHS**](MRHS.md)
  - Class MRHS

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
from MRHS_Solver import LoadFile as lf
from MRHS_Solver import MRHS as ms

mat = lf.load_file("input.txt")
mrhs = ms.MRHS(mat)
mrhs.print_mrhs()
```

##### Create MRHS and fill it with random

```python
from MRHS_Solver import MRHS as ms
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
mrhs.fill_random()
```

##### Create Ctype MRHS and fill it with random
```python
from MRHS_Solver.CTypes.CTypeMRHS import CTypeMRHS

cmrhs = CTypeMRHS()
cmrhs.create_mrhs_fixed(12, 6, 3, 4)
cmrhs.fill_mrhs_random()
mrhs = cmrhs.get_py_mrhs()
```
##### Solve MRHS using python with echelon reduction

```python
from MRHS_Solver import MRHS as ms
from MRHS_Solver.SolveMRHS import find_all_solutions_recursively
from MRHS_Solver.EchelonMRHS import create_echelon_mrhs

vectors = [
        [
            [[1, 0, 1], [1, 1, 1]], #Block
            [[0, 1, 1], [1, 0, 0]]  #RHS
        ],
        [
            [[1, 0], [1, 1]], #BLOCK
            [[0, 0], [0, 1]]  #RHS
        ]
    ]
mrhs = ms.MRHS(vectors)
create_echelon_mrhs(mrhs)
sols = find_all_solutions_recursively(mrhs)
```

##### Generate MRHS and solve using C version

```python
from MRHS_Solver.CTypes.CTypeMRHS import CTypeMRHS

cmrhs = CTypeMRHS()

cmrhs.create_mrhs_fixed(12, 6, 3, 4)
cmrhs.fill_mrhs_random()

#Use algorithms : 'rz' or 'hc'
report = cmrhs.solve(10_000, algorithm="rz", save_file="results.txt", report_solutions=0)
#Prints solving results
report.print_results()
```

        


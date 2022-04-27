# MRHS solver implementation
We are a group of developers engaged in the development of MRHS equations and its distribution. In this project, we want to expand the libraries that deal with this issue with our research.

## Usage 





### Function collections

---

#### MRHS_Solver
- [**MRHS**](MRHS.md)
  - Class MRHS
- [**RHS**](RHS.md)
  - Class for RHS of BlockMatrix
- [**BlockMatrix**](BlockMatrix.md)
  - Class for block in MRHS

---

#### MRHS_Solver.CTypes

- [**CTypeMRHS**](CTypeMRHS.md) 
  - Wrapper class for C interactions

- [**SolverReport**](SolverReport.md)
  - Solver report class for C implementation 
  
- [*Structs*](CStructs.md)


#### Examples

##### Create MRHS from file
```python
from MRHS_Solver import MRHS as ms
mrhs = ms.MRHS()
mrhs.init_with_file("input.txt")
mrhs.print_mrhs()
```

##### Create MRHS with vectors
```python
from MRHS_Solver import MRHS as ms
vectors = [
        [
            [[1, 0, 1], [1, 1, 1]], #BLOCK
            [[0, 1, 1], [1, 0, 0]]  #RHS
        ],
        [
            [[1, 0], [1, 1]], #BLOCK
            [[0, 0], [0, 1]]  #RHS
        ]
    ]
mrhs = ms.MRHS(vectors)
mrhs.print_mrhs()

# or:

mrhs = ms.MRHS()
mrhs.init_with_vectors(vectors)
mrhs.print_mrhs()
```

##### Create MRHS and fill it with random
```python
from MRHS_Solver import MRHS as ms
mrhs = ms.MRHS()
mrhs.init_random(10, 5, [3, 3, 3, 3, 3], [4, 4, 4, 4, 4])
mrhs.print_mrhs()
```

##### Create Ctype MRHS and fill it with random
```python
from MRHS_Solver.CTypes.CTypeMRHS import CTypeMRHS

cmrhs = CTypeMRHS()
cmrhs.create_mrhs_fixed(12, 6, 3, 4)
cmrhs.fill_mrhs_random()
mrhs = cmrhs.get_py_mrhs()
```

##### Solve MRHS recursively using python with echelon reduction

```python
from MRHS_Solver import MRHS as ms

mrhs = ms.MRHS()
mrhs.init_random(10, 5, [3, 3, 3, 3, 3], [4, 4, 4, 4, 4])
solutions = mrhs.solve(method='r')
print(solutions)
```

##### Solve MRHS with brute force

```python
from MRHS_Solver import MRHS as ms

mrhs = ms.MRHS()
mrhs.init_random(8, 5, [3, 3, 3, 3, 3], [4, 4, 4, 4, 4])
solutions = mrhs.solve(method='bf')
print(solutions)
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

#### Convert MRHS to echelon form
```python
from MRHS_Solver import MRHS as ms
mrhs = ms.MRHS()
mrhs.init_random(10, 5, [3, 3, 3, 3, 3], [4, 4, 4, 4, 4])
mrhs.convert_to_echelon()
mrhs.print_mrhs()
```


##### Write MRHS to a file
```python
from MRHS_Solver import MRHS as ms
mrhs = ms.MRHS()
mrhs.init_random(10, 5, [3, 3, 3, 3, 3], [4, 4, 4, 4, 4])
mrhs.convert_to_file("output.txt")
```

        


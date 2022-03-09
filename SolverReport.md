[MRHS_Solver.CTypes](README.md#MRHS_Solver.CTypes)

# Class: **SolverReport**

## Parameters:

- **run_time** : float
  - solver run time
- **xor_count** : int
  - number of xors
- **found_solutions** : int
  - number of found solutions
- **results** : list[int]
  - list of all results
  
## Functions:

- [```print_results()```](#print-results)
- [```get_solution() -> int```](#get-solution)

---

### Print Results

```print_results()```

- Description:
  - Prints out formated Solver report


### Get Solution

```get_solution() -> int```

- Description:
  - Get next solution from generator
- Return:
  - Returns int number of solution, None if there is none or was last  
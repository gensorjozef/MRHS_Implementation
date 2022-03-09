# Class: **CTypeMrhs** 
 
## Parameters:

### c_system:MRHS_System 

- CType MRHS representation

## Functions:

###  ```__init__(mrhs = None:MRHS)```:
- Description
  - Initialization function that creates CType MRHS
- Parameters:
  - **mrhs** : python representation of MRHS
  
### ```set_py_mrhs(mrhs:MRHS)```:

- Description: 
  - Sets python type MRHS and updates CType MRHS
- Parameters:
  - **mrhs**: python representation of MRHS

### ```get_py_mrhs()```:

- Description:
  - Gets python representation of CType MRHS
- Return:
  - **mrhs**: python representation of MRHS
  
### ```solve_hc(maxt: int)```:

- Description:
  - Solves MRHS using hill climbing algorithm
- Parameters:
  - **mrhs**: python representation of MRHS

### ```create_mrhs_fixed(nrows: int, nblocks: int, blocks_size:int, rhs_count: int)```:

- Description:
  - Creates matrix with fixed amount of columns and rhs in each block
- Parameters:
  - **nrows**: number of rows
  - **nblocks**: number of blocks
  - **blocks_size**: number of columns in block
  - **rhs_count**: number of rhs in block
 
### ```create_mrhs_variable(nrows: int, nblocks: int, blocks_sizes:list[int], rhs_counts: list[int])```:

- Description:
  - Creates matrix with fixed amount of collumns and rhs in each block
- Parameters:
  - **nrows**: number of rows
  - **nblocks**: number of blocks
  - **blocks_sizes**: number of collumns in each block
  - **rhs_counts**: number of rhs in each block

### ```fill_mrhs_random()```:
- Description:
  - Fills matrix with random value bits
 
### ```fill_mrhs_random_sparse()```:
- Description:
  - Fills matrix random sparse

### ```fill_mrhs_random_sparse_extra(density: int)```:
- Description:
  - Fills matrix random sparse with density
- Parameters:
  -  **density**: density of fill
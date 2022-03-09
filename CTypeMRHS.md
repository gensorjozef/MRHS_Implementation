# Class: **CTypeMrhs** 
 
## Parameters:

### c_system:MRHS_System 

- CType MRHS representation

## Functions:

- [```__init__(mrhs = None:MRHS)```](#init)

- [```set_py_mrhs(mrhs:MRHS)```](#set-python-mrhs)

- [```get_py_mrhs()```](#get-python-mrhs)

- [```solve_hc(maxt: int)```](#solve-hillclimbing)

- [```create_mrhs_fixed(nrows: int, nblocks: int, blocks_size:int, rhs_count: int)```](#create-mrhs-fixed)

- [```create_mrhs_variable(nrows: int, nblocks: int, blocks_sizes:list[int], rhs_counts: list[int])```](#create-mrhs-variable)

- [```fill_mrhs_random()```](#fill-mrhs-random)

- [```fill_mrhs_random_sparse()```](#fill-mrhs-random-sparse)

- [```fill_mrhs_random_sparse_extra(density: int)```](#fill-mrhs-random-sparse-extra)


### Init

 ```__init__(mrhs = None:MRHS)```:
- Description
  - Initialization function that creates CType MRHS
- Parameters:
  - **mrhs** : python representation of MRHS
  
### Set Python MRHS

 ```set_py_mrhs(mrhs:MRHS)```:

- Description: 
  - Sets python type MRHS and updates CType MRHS
- Parameters:
  - **mrhs**: python representation of MRHS

### Get Python MRHS

```get_py_mrhs()```:

- Description:
  - Gets python representation of CType MRHS
- Return:
  - **mrhs**: python representation of MRHS
 
### Solve HillClimbing 

 ```solve_hc(maxt: int)```:

- Description:
  - Solves MRHS using hill climbing algorithm
- Parameters:
  - **mrhs**: python representation of MRHS

### Create MRHS Fixed

 ```create_mrhs_fixed(nrows: int, nblocks: int, blocks_size:int, rhs_count: int)```:

- Description:
  - Creates matrix with fixed amount of columns and rhs in each block
- Parameters:
  - **nrows**: number of rows
  - **nblocks**: number of blocks
  - **blocks_size**: number of columns in block
  - **rhs_count**: number of rhs in block
 
### Create MRHS Variable

```create_mrhs_variable(nrows: int, nblocks: int, blocks_sizes:list[int], rhs_counts: list[int])```:

- Description:
  - Creates matrix with fixed amount of collumns and rhs in each block
- Parameters:
  - **nrows**: number of rows
  - **nblocks**: number of blocks
  - **blocks_sizes**: number of collumns in each block
  - **rhs_counts**: number of rhs in each block

### Fill MRHS Random

 ```fill_mrhs_random()```:
- Description:
  - Fills matrix with random value bits
 
### Fill MRHS Random Sparse

 ```fill_mrhs_random_sparse()```:
- Description:
  - Fills matrix random sparse

### Fill MRHS Random Sparse Extra

```fill_mrhs_random_sparse_extra(density: int)```:
- Description:
  - Fills matrix random sparse with density
- Parameters:
  -  **density**: density of fill
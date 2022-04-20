[MRHS solver implementation](README.md)

# **Load File**

## Parameters:

- **filename** : string
  - name of input file

  
## Functions:

- [```get_matrix(int: blocksNumber, list[int]: words, int: rowsNumber) -> list[int]```](#print-results)
- [```get_rhs(int: blocksNumber, int: rowsNumber, list[int]: blocksAnswersLen, list[int]: words) -> list[int]```](#get-solution)
- [```get_final_matrix(int: blocksNumber, list[int]: matrix, list[int]: rhs) -> list[int]```](#get-solution)
- [```load_file(string: filename) -> list[int]```](#get-solution)
---

### Get Matrix

```get_matrix(int: blocksNumber, list[int]: words, int: rowsNumber) -> list[int]```

- Description:
  - Internal function to andle matrix from the file for further processing
- Return:
  - Retuns rows and solutions corresponding to block

### Get RHS

```get_rhs(int: blocksNumber, int: rowsNumber, list[int]: blocksAnswersLen, list[int]: words) -> list[int]```

- Description:
  - Internal function to load solutions
- Return:
  - Retuns solutions in RHS form

### Get Final Matrix

```get_final_matrix(int: blocksNumber, list[int]: matrix, list[int]: rhs) -> list[int]```

- Description:
  - Internal function for the final connection of right and left sides
- Return:
  - Retuns rows and solutions corresponding to block

### Load File

```load_file(string: filename) -> list[int]```

- Description:
  - Transform matrix from file to mrhs form
- Return:
  - Returns 2D array, where index corresponds to one block that contains two nested fields => block line, solutions
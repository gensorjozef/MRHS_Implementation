[MRHS_Solver](README.md#MRHS_Solver)

# Class: **MRHS**

## Methods:

- [```print_mrhs(self)```](#print-mrhs) 
- [```init_with_vectors(self, list[list[int]]: vectors)```](#initializes-mrhs-from-vectors) 
- [```init_random(self, int: rows, int: block_num, list[int]: block_lens, list[int]: rhs_lens)```](#initializes-a-random-mrhs)
- [```init_with_file(self, string: file_name)```](#initializes-mrhs-from-a-file)
- [```solve(self, method='r','bf')```](#solve)
- [```convert_to_echelon(self)```](#convert-to-echelon-form)
- [```convert_to_file(self, string: file_name)```](#convert-to-file)

### Print MRHS
 ```print_mrhs(self)```:
- Description
  - Function that prints formated MRHS.

---

### Initializes MRHS from vectors
 ```init_with_vectors(self, list[list[int]]: vectors)```:
- Description
  - Initializes a MRHS from vectors.

---

### Initializes a random MRHS
 ```init_random(self, int: rows, int: block_num, list[int]: block_lens, list[int]: rhs_lens)```:
- Description
  - Checks if parameters are valid. If yes, it initializes a random MRHS.

---

### Initializes MRHS from a file
 ```init_with_file(self, string: file_name)```:
- Description
  - Initializes a MRHS from a file.

---

### Solve
 ```solve(self, method='r','bf')```
- Description
  - Solves MRHS based on method selected.
- Parameters:
  - 'r' -> Finds all solutions to echelonized MRHS using recursive function and transforms them using identity matrix from MRHS.
  - 'bf' -> Finds solutions to MRHS via brute forcing all possible vectors.
- Return:
  - ***list[list[int]]***: list of solutions to MRHS

---

### Convert to echelon form
 ```convert_to_echelon(self)```:
- Description
  - Function that puts MRHS into an echelon form.

---

### Convert to file
 ```convert_to_file(self, string: file_name)```:
- Description
  - Writes MRHS into a file.



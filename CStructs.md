[MRHS_Solver.CTypes](README.md#MRHS_Solver.CTypes)

#List

- [_bm](#_bm)
- [MRHS_system](#mrhs_system)


# _bm

- **nrows**: c_int
- **ncols**: c_int
- **rows**: POINTER(c_uint64)

# MRHS_system

- **nblocks**: c_int 
- **pM**: POINTER([_bm](#_bm))
- **pS**: POINTER([_bm](#_bm))

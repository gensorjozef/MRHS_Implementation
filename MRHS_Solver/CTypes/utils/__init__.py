import typing
from ctypes import c_uint64
from MRHS_Solver.CTypes.CStructs import _bm


def convert_bits_to_long(ar: list[int]) -> c_uint64:
    val: c_uint64 = c_uint64(0)
    for j in range(len(ar)):
        val.value = val.value << 1
        val.value = val.value | ar[j]
    return val


def convert_matrix_to_cblock(matrix: list[list[int]]) -> _bm:
    values_mat: list[c_uint64] = []
    for h in range(len(matrix)):
        vec: list[int] = matrix[h]
        val: c_uint64 = convert_bits_to_long(vec)
        values_mat.append(val)

    cblock = _bm()
    cblock.nrows = len(matrix)
    cblock.ncols = len(matrix[0])
    cblock.rows = (c_uint64*len(values_mat))(*values_mat)
    return cblock


def bitfield(n):
    return [int(digit) for digit in bin(n)[2:]]
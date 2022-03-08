from ctypes import Structure, POINTER, c_int, c_uint64


class _bm(Structure):
    _fields_ = [
                ('nrows', c_int),
                ('ncols', c_int),
                ('rows', POINTER(c_uint64))
                ]


class MRHS_system(Structure):
    _fields_ = [('nblocks', c_int),
                ('pM', POINTER(_bm)),
                ('pS', POINTER(_bm)),
                ]

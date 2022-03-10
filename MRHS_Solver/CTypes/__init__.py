import ctypes.util
from MRHS_Solver.CTypes.CStructs import MRHS_system
from ctypes import *
import os.path
import platform


dll_name: str
if (platform.system() == "Windows"):
    dll_name = "MRHS.dll"
elif (platform.system() == "Linux"):
    dll_name = "MRHS.so"
else:
    raise Exception("Unsupported operating system (Supported= Windows,Linux )")

dll_absolute_path = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + dll_name
mrhs_lib = ctypes.CDLL(dll_absolute_path)

# function prototypes
mrhs_lib.wrapped_solve_rz_file_out.argtypes = (MRHS_system, c_int, POINTER(c_longlong), POINTER(c_longlong), POINTER(c_longlong),c_int,c_char_p )
mrhs_lib.wrapped_solve_hc_file_out.argtypes = (MRHS_system, c_int, POINTER(c_longlong), POINTER(c_longlong), POINTER(c_longlong),c_int,c_char_p )
mrhs_lib.wrapped_solve_rz.argtypes = (MRHS_system, c_int, POINTER(c_longlong), POINTER(c_longlong), POINTER(c_longlong), c_int, CFUNCTYPE(c_int, c_longlong))
mrhs_lib.wrapped_solve_hc.argtypes = (MRHS_system, c_int, POINTER(c_longlong), POINTER(c_longlong), POINTER(c_longlong), c_int, CFUNCTYPE(c_int, c_longlong))


mrhs_lib.wrapped_create_mrhs_fixed.argtypes = (c_int, c_int, c_int, c_int)
mrhs_lib.wrapped_create_mrhs_fixed.restype = POINTER(MRHS_system)

mrhs_lib.wrapped_create_mrhs_variable.argtypes = (c_int, c_int, POINTER(c_int), POINTER(c_int))
mrhs_lib.wrapped_create_mrhs_variable.restype = POINTER(MRHS_system)


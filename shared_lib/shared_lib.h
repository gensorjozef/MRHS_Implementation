#pragma once

#include "mrhs.h"

#ifndef Linux
#ifdef MATHLIBRARY_EXPORTS
#define MATHLIBRARY_API __declspec(dllexport)
#else
#define MATHLIBRARY_API __declspec(dllimport)
#endif
#endif
#ifdef Linux
#define MATHLIBRARY_API __attribute__((visibility("default")))
#endif

#ifdef __cplusplus
extern "C" {
#endif

	/// system (Structure) 
	/// maxt (Number)
	/// pCount (Number Pointer) 
	/// pRestarts (Number Pointer)
	/// results (Array Pointer)
	/// saveCount (Number)
	/// solutionFunction
	/// filename (Char Array Pointer)

	MATHLIBRARY_API long long int wrapped_solve_rz_file_out(MRHS_system system, int maxt, long long int* pCount, long long int* pRestarts, long long int* results, int saveCount, const char* filename);

	MATHLIBRARY_API long long int wrapped_solve_hc_file_out(MRHS_system system, int maxt, long long int* pCount, long long int* pRestarts, long long int* results, int saveCount, const char* filename);

	MATHLIBRARY_API long long int wrapped_solve_rz(MRHS_system system, int maxt, long long int* pCount, long long int* pRestarts, long long int* results,int saveCount, void (*solutionfunction)(long long));

	MATHLIBRARY_API long long int wrapped_solve_hc(MRHS_system system, int maxt, long long int* pCount, long long int* pRestarts, long long int* results,int saveCount, void (*solutionfunction)(long long));

	MATHLIBRARY_API MRHS_system* wrapped_create_mrhs_fixed(int nrows, int nblocks, int blocksize, int rhscount);

	MATHLIBRARY_API MRHS_system* wrapped_create_mrhs_variable(int nrows, int nblocks, int* blocksizes, int* rhscounts);

	MATHLIBRARY_API void wrapped_clear_MRHS(MRHS_system* system);

	MATHLIBRARY_API void wrapped_fill_mrhs_random(MRHS_system* psystem);

	MATHLIBRARY_API void wrapped_fill_mrhs_random_sparse(MRHS_system* psystem);

	MATHLIBRARY_API void wrapped_fill_mrhs_random_sparse_extra(MRHS_system* psystem, int density);


#ifdef __cplusplus
}
#endif


#define _CRT_SECURE_NO_WARNINGS
#include "shared_lib.h"
#include "mrhs.hillc.h"
#include "mrhs.rz.h"
//#include "pch.h"

long long int wrapped_get_next_solution(MRHS_system* system) {
	return 0ll;
}

long long int wrapped_solve_rz_file_out(MRHS_system system, int maxt, long long int* pCount, long long int* pRestarts, long long int* result, int saveCount, const char* filename)
{
	FILE* file = fopen(filename, "w");
	long long int ret = solve_rz(system, maxt, pCount, pRestarts, file);
	fclose(file);
	return ret;
}

long long int wrapped_solve_hc_file_out(MRHS_system system, int maxt, long long int* pCount, long long int* pRestarts, long long int* result, int saveCount, const char* filename)
{
	FILE* file = fopen(filename, "w");
	long long int ret = solve_hc(system, maxt, pCount, pRestarts, file);
	fclose(file);
	return ret;
}

long long int wrapped_solve_rz(MRHS_system system, int maxt, long long int* pCount, long long int* pRestarts, long long int* results, int saveCount)
{
	return solve_rz(system, maxt, pCount, pRestarts,NULL);
}

long long int wrapped_solve_hc(MRHS_system system, int maxt, long long int* pCount, long long int* pRestarts, long long int* results, int saveCount)
{
	return solve_hc(system,maxt,pCount,pRestarts,NULL);
}

MRHS_system* wrapped_create_mrhs_fixed(int nrows, int nblocks, int blocksize, int rhscount) {
	 return create_mrhs_fixed(nrows, nblocks, blocksize, rhscount);;
}

MRHS_system* wrapped_create_mrhs_variable(int nrows, int nblocks, int* blocksizes, int* rhscounts) {
	return create_mrhs_variable(nrows, nblocks, blocksizes, rhscounts);
}

void wrapped_clear_MRHS(MRHS_system* system) {
	clear_MRHS(system);
}
void wrapped_fill_mrhs_random(MRHS_system* psystem) {
	fill_mrhs_random(psystem);
}
void wrapped_fill_mrhs_random_sparse(MRHS_system* psystem) {
	fill_mrhs_random_sparse(psystem);
}
void wrapped_fill_mrhs_random_sparse_extra(MRHS_system* psystem, int density) {
	fill_mrhs_random_sparse_extra(psystem, density);
}
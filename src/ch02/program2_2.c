#include <stdio.h>
#include <stdlib.h>

#define M 2 /* 行の要素数 */
#define N 3 /* 列の要素数 */

/* 行列の領域確保 */
double **dmatrix(int nr1, int nr2, int nl1, int nl2);
/* 行列の領域解放 */
void free_dmatrix(double **a, int nr1, int nr2, int nl1, int nl2);

int main(void)
{
	double **a;
	int i, j;

	a = dmatrix(1, M, 1, N); /* メモリの確保 */

	for(i = 1; i <= M; i++){  /* 要素の代入 */
		for(j = 1; j <= N; j++){
			a[i][j] = (i + j) / 2.0;
			printf("a[%d][%d] = %f \n", i, j, a[i][j]);
		}
	}
	free_dmatrix(a, 1, M, 1, N);  /* メモリの解放 */

	return 0;
}

double **dmatrix(int nr1, int nr2, int nl1, int nl2)
{
	int i, nrow, ncol;
	double **a;

	nrow = nr2 - nr1 + 1; /* 行の数 */
	ncol = nl2 - nl1 + 1; /* 列の数 */

	/* 行の確保 */
	if((a = malloc(nrow * sizeof(double *)) )== NULL){
		printf("メモリが確保できません (行列 a)\n");
		exit(1);
	}
	a = a - nr1; /* 行をずらす */

	/* 列の確保 */
	for(i = nr1; i <= nr2; i++) a[i] = malloc(ncol * sizeof(double));
	for(i = nr1; i <= nr2; i++) a[i] = a[i] - nl1;                    /* 列をずらす */

	return (a);
}

void free_dmatrix(double **a, int nr1, int nr2, int nl1, int nl2)
{
	int i;

	/* メモリの解放 */
	for(i = nr1; i <= nr2; i++) free((void *)(a[i] + nl1));
	free((void *)(a + nr1));
}
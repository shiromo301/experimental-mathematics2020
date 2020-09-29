#include <stdio.h>
#include <stdlib.h>

#define N 5 /* 要素数の指定 */

double *dvector(int i, int j); /* ベクトル領域の確保 */
void free_dvector(double *a, int i); /* 領域の解放 */

/* ベクトル a[m...n] と b[m...n] の内積を計算する */
double inner_product(int m, int n, double *a, double *b);

int main(void)
{
	double *a, *b;
	int i;

	/* ベクトルの定義, 配列 a,b ̓の添字は 1～N */
	a = dvector(1,N); b = dvector(1,N);
	for(i = 1;i <= N;i++){
		a[i] = (double)i / 20.0;
		b[i] = (double)i / 10.0;
	}

	printf("aとbの内積は%f です\n", inner_product(1, N, a, b));
	free_dvector(a,1); free_dvector(b,1);

	return 0;
}

/* ベクトル a[m...n] と b[m...n] の内積を計算する */
double inner_product(int m, int n, double *a, double *b)
{
	int i;
	double s = 0.0;

	for (i = m; i <= n; i++)
		s += a[i] * b[i];

	return s;
}

double *dvector(int i, int j)  /* a[i]～a[j] の領域を確保 */
{
	double *a;

	if((a = malloc( ((j - i + 1) * sizeof(double))) ) == NULL)
	{
		printf("メモリが確保できません (from dvector) \n");
			exit(1);
	}

	return (a - i);
}

void free_dvector(double *a, int i)
{
	free( (void *)(a + i) ); /* (void *) 型へのキャストが必要 */
}
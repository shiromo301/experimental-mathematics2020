#include <stdio.h>
#include <stdlib.h>

#define N 5 /* 要素数の指定 */

double *dvector(int i, int j); /* ベクトル領域の確保 */
void free_dvector(double *a, int i); /* 領域の解放 */

int main(void)
{
	double *a, *b;
	int i;

	printf("a の領域確保\n"); /* 配列 a の添字は 1～N */
	a = dvector(1,N);
	for(i = 1; i <= N; i++){
		a[i] = (double)i / 20.0;
		printf("a[%d] = %f \n", i, a[i]);
	}
	free_dvector(a,1);
	printf("aを解放しました\n");

	printf("bの領域確保\n");
	b = dvector(2,N+1);		/* 配列 b の添字は 2～N+1 */
	for(i = 2; i <= N+1; i++){
		b[i] = (double)i / 20.0;
		printf("b[%d] = %f \n", i, b[i]);
	}
	free_dvector(b,2);
	printf("b を解放しました\n");

	return 0;
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
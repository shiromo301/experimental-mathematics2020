#include <stdio.h>
#include <stdlib.h>  /* qsort 関数を使うために必要 */

#define N 7

/* 比較関数 (昇順) */
int double_comp(const void *s1, const void *s2);

int main(void)
{
	double a[N] = {1.2, -2.3, -4.2, 5.5, 2.1, 7.2, 3.1};
	int i;

	qsort(a, N, sizeof(a[0]), double_comp); /* 並べ換え */

	for(i = 0; i < N; i++) printf("%f\n", a[i]);

	return 0;
}

/* 比較関数 (昇順) */
int double_comp(const void *s1, const void *s2)
{
	const double a1 = *((double *)s1); /* (double *) へキャスト */
	const double a2 = *((double *)s2); /* (double *) へキャスト */
	if(a1 < a2){
		return -1;
	}else if(a1 == a2){
		return 0;
	}else{
		return 1;
	}
}
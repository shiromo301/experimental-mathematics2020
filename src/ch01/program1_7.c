#include <stdio.h>

int main(void)
{
	double deps = 1.0;	/* マシンイプシロン (double 型) */
	double dtmp;	/* 作業用変数 (double 型) */
	float feps = 1.0;	/* マシンイプシロン (float 型) */
	float ftmp;		/* 作業用変数(float 型) */

	/* double 型のマシンイプシロンの計算 */
	/* deps + 1 > 1 の間, deps を 2 で割り続ける */
	for(dtmp = deps + 1.0; dtmp > 1; deps /= 2.0, dtmp = deps + 1.0);
	printf("double 型の Machine epsilon は %-16g\n", 2.0 * deps);
	printf("double 型の Unit roundoff は %-16g\n", deps);

	/* float 型のマシンイプシロンの計算 */
	/* feps + 1 > 1 の間, feps を 2 で割り続ける */
	for(ftmp = feps + 1.0; ftmp > 1; feps /= 2.0, ftmp = feps + 1.0);
	printf("float 型の  Machine epsilon は %-16g\n", 2.0 * feps);
	printf("float 型の Unit roundoff は %-16g\n", feps);

	return 0;
}
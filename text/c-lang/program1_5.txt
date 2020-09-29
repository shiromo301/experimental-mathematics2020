#include <stdio.h>

int main(void)
{
	double a, b;
	a = 1.0 / 0.0;  /* 無限大の生成 */
	printf("a=%f \n", a);
	b = 1.0 / a;  /* 無限大による除算 */
	printf("b=%f \n", b);
	return 0;
}
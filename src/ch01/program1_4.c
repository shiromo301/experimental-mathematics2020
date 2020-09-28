#include <stdio.h>

int main(void)
{
	double a, b;
	a = 0.0 / 0.0;  /* NaNの生成 */
	printf("a=%f \n", a);
	b = 1.0 + a;  /* NaNによる演算 */
	printf("b=%f \n", b);
	return 0;
}
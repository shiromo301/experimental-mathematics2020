#include <stdio.h>

int main(void)
{
	double a, b, c, d;
	a = 1.0 / 0.0;  b = -1.0 / 0.0;		/* inf の生成 */
	printf("a=%f b=%f \n", a, b);
	c = 1.0 / a;	d = 1.0 / b;		/* 符号付きゼロの生成 */
	printf("c=%f d=%f \n", c, d);
	printf("ans1=%f, ans2=%f\n", 1.0 / c, 1.0 / d);

	return 0;
}
#include <stdio.h>

int main(void)
{
	char x = 123, y;

	y = x & 0xf0;
	printf("x = %d, y = %d\n", x, y);

	return 0;
}
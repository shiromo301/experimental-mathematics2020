#include <stdio.h>

int main(void)
{
	unsigned char x = 1, y;

	y = x << 6;
	printf("x = %d, y = %d\n", x, y);

	return 0;
}
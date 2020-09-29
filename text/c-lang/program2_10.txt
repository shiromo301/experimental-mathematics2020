/*   0.1を N 回加えるプログラム */
#include <stdio.h>

#define N 1000000

int main(void)
{
  double s, e, y, tmp;
  int i;

  /* Recursive summation */
  s = 0.0;
  for ( i = 1; i <= N; i++ ) s += 0.1 ;
  printf("Recursive summation の結果は\t %30.20f \n", s);

  /* Compensated summation*/
  s = 0.0; e = 0.0;
  for ( i = 1; i <= N; i++ )
  {
    tmp = s;
    y = 0.1 + e;                
    s = tmp + y;                
    e = (tmp - s) + y;
  }
  printf("Compensated summation の結果は\t %30.20f \n", s);

  return 0;
}

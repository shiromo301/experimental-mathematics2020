#include <stdio.h>

/* 関数の定義 */
double func(double x, double y);
/* オイラー法 */
void euler(double x, double y, double a, double b, int n, 
                               double (*f)(double, double) );

int main(void)
{
  int n;

  printf("分割数を入力してください--->");
  scanf("%d",&n);

  euler( 0.0, 1.0, 0.0, 1.0, n, func );

  return 0;
}

/* オイラー法 */
void euler(double x, double y, double a, double b, int n, 
                               double (*f)(double, double) )
{
  double h;
  int i;

  h = (b-a)/n;  /* 刻み幅 */

  for ( i = 0 ; i < n ; i++)
  {
    y = y + h * (*f)(x,y); 
    x += h;
    printf("x=%f \t y=%f \n", x, y );
  }
}

/* 関数の定義 */
double func(double x, double y)
{
  return( x + y );
}

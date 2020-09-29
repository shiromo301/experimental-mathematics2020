#include <stdio.h>

/* 関数の定義 */
double func(double x, double y);
/* ホイン法 */
void heun(double x, double y, double a, double b, int n,
                              double (*f)(double, double) );

int main(void)
{
  int n;

  printf("分割数を入力してください--->");
  scanf("%d",&n);

  heun( 0.0, 1.0, 0.0, 1.0, n, func );

  return 0;
}

/* ホイン法 */
void heun(double x, double y, double a, double b, int n,
                              double (*f)(double, double) )
{
  double k1, k2, h;
  int i;

  h = (b-a)/n;

  for ( i = 0 ; i < n ; i++)
  {
    k1 = f(x,y); k2 = f(x+h, y+h*k1);
    y = y + h/2.0 * ( k1 + k2 );
    x += h;
    printf("x=%f \t y=%f \n", x, y );
  }

}

/* 関数の定義 */
double func(double x, double y)
{
  return( x + y );
}

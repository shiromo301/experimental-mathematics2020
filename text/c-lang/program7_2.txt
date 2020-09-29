#include <stdio.h>

/* 関数の定義 */
double func1(double x);
double func2(double x);
/* シンプソン項式 */
double simpson( double a, double b, int n, double (*f)(double) );

int main(void)
{
  int n=50;

  printf("2.0/(x*x) を [1,2]で積分します. 分割数は%d です\n", 2*n);
  printf("結果は%20.15f です\n",simpson(1.0, 2.0, n, func1) );

  printf("4.0/(1+x*x) を [0,1]で積分します. 分割数は%d です\n", 2*n);
  printf("結果は%20.15fです\n",simpson(0.0, 1.0, n, func2) );

  return 0;
}

/* シンプソン項式 */
double simpson( double a, double b, int n, double (*f)(double) )
{
  double S, h;
  int i;

  h = ( b - a ) /( 2.0*n ) ;  /* 刻み幅の指定 */

  /* シンプソン項式 */
  S = ( (*f)(a) + (*f)(b) ) ;
  for ( i = 1; i < n; i++)
  {
    S += 4.0*(*f)( a + (2.0*i-1.0)*h ) + 2.0*(*f)( a + 2.0*i*h );
  }
  S += 4.0*(*f)( a + (2.0*n-1.0)*h );
  S *= h/3.0;

  return S;
}

/* 関数の定義 */
double func1(double x)
{
  return( 2.0/(x*x) );
}

double func2(double x)
{
  return( 4.0 / (1.0+x*x) );
}

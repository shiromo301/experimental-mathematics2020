#include <stdio.h>

/* 関数の定義 */
double func1(double x);
double func2(double x);
/* 台形公式 */
double trapezoidal( double a, double b, int n, double (*f)(double) );

int main(void)
{
  int n=100;

  printf("2.0/(x*x) を [1,2] で積分します. 分割数は%d です\n", n);
  printf("結果は%20.15f です\n",trapezoidal(1.0, 2.0, n, func1) );

  printf("4.0/(1+x*x) を [0,1] で積分します. 分割数は%d です\n", n);
  printf("結果は%20.15f です\n",trapezoidal(0.0, 1.0, n, func2) );

  return 0;
}

/* 台形公式 */
double trapezoidal( double a, double b, int n, double (*f)(double) )
{
  double T, h;
  int i;

  h = ( b - a ) /n ;  /* 刻み幅の指定 */

  /* 関数の定義 */
  T = ( (*f)(a) + (*f)(b) ) / 2.0; 
  for ( i = 1; i < n; i++) T += (*f)( a + i*h ); 
  T *= h;

  return T;
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

#include <stdio.h>
#include <stdlib.h>

/* 被積分関数の定義 */
double func(double x, double y);

/* y の積分区間  */
double phi(double x);
double psi(double x);

/* ベクトル領域の確保 */
double *dvector(int i, int j);  
/* ベクトル領域の解放 */
void free_dvector(double *a, int i); 

/* 重積分用の台形公式 */
double trapezoidal2( double a, double b, int m, int n, double (*p)(double), 
                     double (*q)(double), double (*f)(double,double) );
int main(void)
{
  int n=20, m=20;

  printf("8x^2+4y を x=[1,2], y=[2-x,x^2] で積分します \n");
  printf("x の分割数は%d, y の分割数は%d, 結果は%15.10f\n", m, n, 
           trapezoidal2( 1.0, 2.0, m, n, phi, psi, func ) );
  
  return 0;
}

/* 重積分の台形公式 */
double trapezoidal2( double a, double b, int m, int n, double (*p)(double), 
                     double (*q)(double), double (*f)(double,double) )
{
  double T, h, k, *F, x, y1, y2; 
  int i, j;

  F = dvector( 0, n ); 
  h = ( b - a ) /n ;          /* 刻み幅の指定(x 方向) */

  /* F_i の計算 */
  for ( i = 0; i <= n; i++ )
  {
    x = a + i*h; 
    y1 = (*p)(x); y2 = (*q)(x);
    k = ( y2 - y1 )/m;         /* 刻み幅の指定(y 方向) */
    F[i] = ( (*f)(x, y1) + (*f)(x, y2) ) / 2.0;
    for ( j = 1; j < m; j++ )  F[i] += (*f)(x, y1+j*k);
    F[i] *= k; 
  }

  /* 積分の計算 */
  T = ( F[0] + F[n] ) / 2.0; 
  for ( i = 1; i < n; i++) T += F[i]; 
  T *= h;

  free_dvector( F, 0 ); 

  return T;
}

/* 被積分関数の定義 */
double func(double x, double y)
{
  return( 8.0*x*x + 4.0*y );
}

/* y の積分区間  */
double phi(double x)
{
  return( 2.0-x );
}

double psi(double x)
{
  return( x*x );
}

double *dvector(int i, int j) /* a[i]～a[j] の領域を確保 */
{
  double *a;

  if ((a = malloc(((j - i + 1) * sizeof(double)))) == NULL)
  {
    printf("メモリが確保できません (from dvector) \n");
    exit(1);
  }

  return (a - i);
}

void free_dvector(double *a, int i)
{
  free((void *)(a + i)); /* (void *) 型へのキャストが必要 */
}

#include <stdio.h>
#include <math.h>

#define EPS  pow(10.0,-8.0)   /* epsilon の設定 */
#define NMAX 100            /* 最大反復回数 */

void newton1( double x );    /* Newton法(重複次数付き) */
double f(double x);         /* f(x) の計算 */
double df(double x);        /* f'(x) の計算 */

int main(void)
{
  double x;
  printf("初期値 x0 を入力してください\n");
  scanf("%lf",&x);

  newton1( x );

  return 0;
}

/* Newton法(重複次数つき) */
void newton1( double x )
{
  int n=0; double d, x0=x, x1=x, x2=x, m; /* x で x0,x1,x2 を初期化 */

  do
  {
    d = -f(x)/df(x);
    x = x + d;
    n ++;
    x0 = x1; x1 = x2; x2 = x; 
  }while( fabs(d) > EPS && n < NMAX);

  m = (x0 - x1)/(x0 - 2.0*x1 + x2) ; /* 重複次数の計算 */
  if ( n == NMAX )
  {
    printf("答えが見つかりませんでした\n");
  }
  else
  {
    printf("答えは x=%f で, 重複次数は%fです\n",x, m);
  }

}

/* 関数の定義 */
double f(double x)
{
  return( x*x*x - x*x - x + 1.0 );
}

/* 導関数の定義 */
double df(double x)
{
  return( 3.0*x*x - 2.0*x - 1.0 );
}




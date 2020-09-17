#include <stdio.h>
#include <math.h>

#define EPS  pow(10.0,-8.0)   /* epsilon の設定 */
#define NMAX 10             /* 最大反復回数 */

void newton( double x );    /* Newton 法 */
double f(double x);         /* f(x) の計算 */
double df(double x);        /* f'(x) の計算 */

int main(void)
{
  double x;
  printf("初期値 x0 を入力してください\n");
  scanf("%lf",&x);

  newton( x );

  return 0;
}

/* Newton法 */
void newton( double x )
{
  int n=0; double d;

  do
  {
    d = -f(x)/df(x);
    x = x + d;
    n ++;
  }while( fabs(d) > EPS && n < NMAX);

  if ( n == NMAX )
  {
    printf("答えが見つかりませんでした\n");
  }
  else
  {
    printf("答えは x=%f です\n",x);
  }

}

double f(double x)
{
  return( x-cos(x) );
}

double df(double x)
{
  return( 1.0+sin(x) );
}



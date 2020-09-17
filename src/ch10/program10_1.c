#include <stdio.h>

#define N 6       /* 求める桁数 5*(N+1) 桁 */
#define DEG   100000    /*  桁数の基準  */

void adds(int x[], int y[], int z[]); /* z = x+y */
void subs(int x[], int y[], int z[]); /* z = x-y */
void muls(int x[], int z[], int n ); /* z = x*n */
void divs(int x[], int z[], int n); /* z = x/n */
void print_result(int x[]); /* 表示用関数 */

int main(void)
{
  int x[N+1] = {00002, 12345, 99999, 33333, 44444, 55555, 66666};
  int y[N+1] = {00001, 45678, 88888, 90000, 88888, 77777, 66666};
  int z[N+1];  /* 結果は z へ */

  printf("x = ");  print_result(x); 
  printf("y = ");  print_result(y);
  adds(x, y, z);   printf("x+y=\t"); print_result(z);
  subs(x, y, z);   printf("x-y=\t"); print_result(z);
  muls(x, z, 9999);  printf("x*9999=\t"); print_result(z);
  divs(x, z, 9999);  printf("x/9999=\t"); print_result(z);

  return 0;
}

void adds(int x[], int y[], int z[])
{
  int up, i, sum;
  /* 加算 */
  up = 0;
  for ( i=N; i>=0; i--)
  {
    sum = x[i]+y[i]+up;
    if ( sum > DEG-1 )
    {
      z[i] = sum - DEG;
      up = 1;
    }
    else
    {
      z[i]=sum; up = 0;
    }
  }
}

void subs(int x[], int y[], int z[])
{
  int borrow, i, sub;
  /* 減算 */
  borrow = 0;
  for ( i=N; i>=0; i--)
  {
    sub = x[i]-y[i]-borrow;
    if ( sub >= 0)
    {
      z[i] = sub; borrow = 0;
    }
    else
    {
      z[i] = DEG + sub;
      borrow = 1;
    }
  }
}

void muls(int x[], int z[], int n )
{
  /* 乗算 */
  int i, up=0, prod; 
  for ( i=N; i>=0; i--)
  {
    prod = x[i] * n + up;
    z[i] = prod % DEG;
    up = prod / DEG;
  }
}

void divs(int x[], int z[], int n)
{
  /* 除算 */
  int amari, i, bunshi; 
  amari = 0;
  for ( i=0 ; i<=N; i++)
  {
    bunshi = amari * DEG + x[i];
    z[i] = bunshi/n;
    amari = bunshi % n;
  }
}

void print_result(int x[])
{
  int i;
  for ( i = 0; i <= N; i++)
  {
    printf("%05u ",x[i]);
  }
  printf("\n");
}

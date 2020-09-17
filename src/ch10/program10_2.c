#include <stdio.h>

#define N 200       /* 求める桁数 5*N 桁 */
#define DEG   100000    /*  桁数の基準  */

void init(int a[], int n);
void adds(int a[], int b[], int c[]); /* c = a+b */
void subs(int a[], int b[], int c[]); /* c = a-b */
void divsp(int a[], int b[], int n, int p); /* b = a/n */
int top(int a[], int p); /* 0 でない最左位置, p が大きいほど右へ */
void print_result(int a[]); /* 表示用関数 */
void arctan(int a[], int n, int d); /* n*arctan(1/d) の計算 */

int main(void)
{

  int a[N+1], b[N+1], pi[N+1];

  arctan(a, 16, 5);
  arctan(b, 4, 239);

  subs(a,b,pi);
  print_result(pi);

  return 0;
}

void adds(int a[], int b[], int c[]) 
{
  int up, i, sum;
  /* 加算 */
  up = 0;
  for ( i=N; i>=0; i--)
  {
    sum = a[i]+b[i]+up;
    if ( sum > DEG-1 )
    {
      c[i] = sum - DEG;
      up = 1;
    }
    else
    {
      c[i]=sum; up = 0;
    }
  }
}

void subs(int a[], int b[], int c[])
{
  int borrow, i, sub;
  /* 減算 */
  borrow = 0;
  for ( i=N; i>=0; i--)
  {
    sub = a[i]-b[i]-borrow;
    if ( sub >= 0)
    {
      c[i] = sub; borrow = 0;
    }
    else
    {
      c[i] = DEG + sub;
      borrow = 1;
    }
  }
}

void divsp(int a[], int b[], int bunbo, int p)
{
  /* 除算 */
  int amari, i, bunshi; /* p は配列の番号 */
  amari = 0;
  for ( i=p ; i<=N; i++)
  {
    bunshi = amari * DEG + a[i];
    b[i] = bunshi/bunbo;
    amari = bunshi % bunbo;
  }
}

void print_result(int a[])
{
  int i;

  printf("%5u.",a[0]);
  for ( i = 1; i <= N; i++)
  {
    printf("%05u ",a[i]);
  }
  printf("\n");
}

void arctan(int a[], int n, int d)
{
  int e[N+1], f[N+1], p, i; 

  init(a,0); init(e,n);

  /* (**) の第 1 項の計算 */
  divsp(e, e, d, 0);
  adds(a, e, a);
  p = top(e,0);

  /* (**) の第 2 項の計算 */
  i = 3;
  while( p <= N)
  {
    divsp(e, e, d, p);
    divsp(e, e, d, p);
    divsp(e, f, i, p);
    if (i%4 ==1 )
    {
      adds(a, f, a);
    }
    else
    {
      subs(a, f, a);
    }
    p = top(e, p);
    i += 2;
  }
}

/* 0 でない最左位置 p を探す */
int top(int a[], int p) 
{
  while( p<= N && a[p] == 0) p++;
  return p;
}

/* 値を初期化 a[0]=n で, それ以外は 0 */
void init(int a[], int n)
{
  int i;

  a[0] = n;
  for( i=1; i<=N; i++)
  {
    a[i] = 0;
  }
}


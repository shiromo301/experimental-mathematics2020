#include <stdio.h>
#include <stdlib.h> /* srand, rand 関数を使うために必要 */
#include <time.h>   /* time 関数を使うために必要 */

#define ROW     3 /* 行の要素数 */
#define COLUMN  4 /* 列の要素数 */

/* 行列の領域確保 */
double **dmatrix(int nr1, int nr2, int nl1, int nl2);
/* 行列の領域解放 */
void free_dmatrix(double **a, int nr1, int nr2, int nl1, int nl2);
/* 行列の生成 a[nr1...nr2][nl1...nl2] */
double **produce_matrix( double **a, int nr1, int nr2, int nl1, int nl2);

int main(void)
{
  double **a; 
  int i, j; 

  a = dmatrix(1, ROW, 1, COLUMN); /* 行列 a[1...ROW][1...COLUMN] */
  a = produce_matrix( a, 1, ROW, 1, COLUMN); /* 行列の生成 */

  /* 行列の表示 */
  for ( i = 1 ; i <= ROW ; i++)
  {
    for ( j = 1 ; j <= COLUMN ; j++)
    {
      printf("%f\t",a[i][j]);
    }
    printf("\n");
  } 

  free_dmatrix( a, 1, ROW, 1, COLUMN);   /* 行列領域の解放 */

  return 0;
}

/* 行列の生成 a[nr1...nr2][nl1...nl2] */
double **produce_matrix( double **a, int nr1, int nr2, int nl1, int nl2)
{
  int i, j ;

  srand( (unsigned)time(NULL)); /* シードを与える */
  for ( i = nr1 ; i <= nr2 ; i++)
  {
    for ( j = nl1 ; j <= nl2 ; j++)
    {
      a[i][j] = (double)rand() / (double)RAND_MAX;
    }
  } 
  return a; 
}

double **dmatrix(int nr1, int nr2, int nl1, int nl2)
{
  int i, nrow, ncol;
  double **a;

  nrow = nr2 - nr1 + 1; /* 行の数 */
  ncol = nl2 - nl1 + 1; /* 列の数 */

  /* 行の確保 */
  if ((a = malloc(nrow * sizeof(double *))) == NULL)
  {
    printf("メモリが確保できません (行列 a)\n");
    exit(1);
  }
  a = a - nr1; /* 行をずらす */

  /* 列の確保 */
  for (i = nr1; i <= nr2; i++)
    a[i] = malloc(ncol * sizeof(double));
  for (i = nr1; i <= nr2; i++)
    a[i] = a[i] - nl1; /* 列をずらす */

  return (a);
}

void free_dmatrix(double **a, int nr1, int nr2, int nl1, int nl2)
{
  int i;

  /* メモリの解放 */
  for (i = nr1; i <= nr2; i++)
    free((void *)(a[i] + nl1));
  free((void *)(a + nr1));
}
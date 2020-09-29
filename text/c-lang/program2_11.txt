#include <stdio.h>
#include <stdlib.h> /* srand, rand 関数を使うために必要 */
#include <time.h>   /* time 関数を使うために必要 */

int main(void)
{
  int i; 
 
  printf("シードなし\n");
  for ( i = 1; i <= 2; i++)  printf("%d\t", rand() );
  printf("\n");

  printf("シードつき\n");
  srand( (unsigned)time(NULL)); 
  for ( i = 1; i <= 2; i++)  printf("%d\t", rand() );
  printf("\n");

  return 0;
}

from random import seed

from program2_2 import Dmatrix
from program2_11 import rand, RAND_MAX

ROW    = 3 # 行の要素数
COLUMN = 4 # 列の要素数

def main():
    a = produce_matrix( 1, ROW, 1, COLUMN ) # 行列の生成

    # 行列の表示
    for i in range(1, ROW+1):
        for j in range(1, COLUMN+1):
            print(a[i][j], end="\t")
        print()


def produce_matrix(nr1: int, nr2: int, nl1: int, nl2: int):
    a = Dmatrix(nr1, nr2, nl1, nl2)
    seed() # シードを与える
    for i in range(nr1, nr2+1):
        for j in range(nl1, nl2+1):
            a[i][j] = rand() / RAND_MAX
    return a


if __name__ == "__main__":
    main()
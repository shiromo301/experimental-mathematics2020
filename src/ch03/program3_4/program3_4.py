# TODO: テキストと出力結果が合わないバグを修正

import sys
sys.path.append("../../ch02")

from program2_1 import Dvector
from program2_2 import Dmatrix
from program2_3 import input_vector, input_matrix

N = 4 # N次正方行列

def main():
    global N

    a = Dmatrix(1, N, 1, N) # 行列 a[1...N][1...N]
    b = Dvector(1, N) # b[1...N]

    # ファイルのオープン
    with open("input_cho.dat", "r") as fin:
        with open("output_cho.dat", "w") as fout:
            input_matrix( a, 'A', fin, fout ) # 行列 A の入出力
            input_vector( b, 'b', fin, fout ) # ベクトル b の入出力
            a = cholesky_decomp( a )          # 修正コレスキー分解
            b = cholesky_solve( a, b )        # 前進代入・後退代入

            # 結果の出力
            fout.write("Ax=bの解は次の通りです\n")
            for i in range(1, N+1):
                fout.write(f"{b[i]}\t\n")


# 修正コレスキー分解
def cholesky_decomp(a: Dmatrix):
    for i in range(2, N+1):
        for j in range(1, i):
            tmp = 0.0
            for k in range(1, j):
                tmp += a[i][k] * a[k][k] * a[j][k]
            a[i][j] = (a[i][j] - tmp) / a[j][j]
        tmp = 0.0
        for k in range(1, j):
            tmp += a[i][k] * a[i][k] * a[k][k]
        a[i][i] = a[i][i] - tmp
    return a


# 修正コレスキー分解を利用して連立一次方程式を解く
def cholesky_solve(a: Dmatrix, b: Dvector):
    # LDy = b
    b[1] = b[1] / a[1][1]
    for i in range(2, N+1):
        tmp = 0.0
        for j in range(1, i):
            tmp += a[j][j] * a[i][j] * b[j]
        b[i] = ( b[i] - tmp ) / a[i][i]

    # L^t x = y
    for i in range(N-1, 0, -1):
        tmp = 0.0
        for j in range(i+1, N+1):
            tmp += a[j][i] * b[j]
        b[i] = b[i] - tmp

    return b


if __name__ == "__main__":
    main()
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../ch02'))

from program2_1 import Dvector
from program2_2 import Dmatrix
from program2_3 import input_vector, input_matrix

N = 4 # N次正方行列

def main():
    global N
    a = Dmatrix(1, N, 1, N) # 行列 a[1...N][1...N]
    b = Dvector(1, N) # b[1...N]

    # ファイルのオープン
    with open("input.dat", "r") as fin:
        with open("output.dat", "w") as fout:
            input_matrix( a, 'A', fin, fout ) # 行列 A の入出力
            input_vector( b, 'b', fin, fout ) # ベクトル b の入出力
            b = simple_gauss( a, b )          # ガウス消去法

            # 結果の出力
            fout.write("Ax=b の解は次の通りです\n")
            for i in range(1, N+1):
                fout.write("{:.6f}\n".format(b[i]))


# ガウス消去法
def simple_gauss(a: Dmatrix, b: Dvector):
    # 前進消去
    for k in range(1, N):
        for i in range(k+1, N+1):
            alpha = - a[i][k] / a[k][k]
            for j in range(k+1, N+1):
                a[i][j] += alpha * a[k][j]
            b[i] += alpha * b[k]

    # 後退代入
    b[N] /= a[N][N]
    for k in range(N-1,0,-1):
        tmp = b[k]
        for j in range(k+1, N+1):
            tmp -= a[k][j] * b[j]
        b[k] = tmp / a[k][k]

    return b


if __name__ == "__main__":
    main()
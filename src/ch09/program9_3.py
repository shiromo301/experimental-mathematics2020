import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../ch02'))

from math import sqrt

from program2_1 import Dvector
from program2_2 import Dmatrix
from program2_3 import input_matrix
from program9_2 import householder

N = 4

def main():
    eps = 10.0 ** -8.0

    a = Dmatrix(1, N, 1, N) # 行列領域の確保

    # ファイルのオープン
    with open("input_eigen.dat", "r") as fin:
        with open("result_eigen.dat", "w") as fout:
            input_matrix( a, 'A', fin, fout ) # 行列 A の入出力
            householder( a, N )               # ハウスホルダー法
            qr( a, eps, N )                   # QR法

            # 結果の出力
            print("QR法の結果は")
            for i in range(1, N+1):
                for j in range(1, N+1):
                    print("{:10.7f}\t".format(a[i][j]), end="")
                print()

            print("固有値は")
            for i in range(1, N+1):
                print("{:10.7f}\t".format(a[i][i]), end="")
            print()


# QR法
def qr(a: Dmatrix, eps: float, n: int):
    # 領域の確保
    q    = Dmatrix(1, n, 1, n)
    work = Dvector(1, n)
    m = n
    while m > 1:
        # 収束判定
        if abs(a[m][m-1]) < eps:
            m = m - 1
            continue

        # 原点移動
        s = a[n][n]
        if m == n:  # m=n のときは原点移動なし
            s = 0.0
        for i in range(1, m+1):
            a[i][i] -= s
        
        # QR法
        for i in range(1, m+1):
            for j in range(1, m+1):
                q[i][j] = 0.0      # Q を m x m 単位行列で初期化
            q[i][i] = 1.0
        
        # R と Q の計算
        for i in range(1, m):
            r = sqrt( a[i][i]*a[i][i] + a[i+1][i]*a[i+1][i] )
            if r == 0.0:
                sint = 0.0
                cost = 0.0
            else:
                sint = a[i+1][i] / r
                cost = a[i][i] / r
            for j in range(i+1, m+1):
                tmp = a[i][j]*cost + a[i+1][j]*sint
                a[i+1][j] = -a[i][j]*sint + a[i+1][j]*cost
                a[i][j] = tmp
            a[i+1][i] = 0.0
            a[i][i] = r
            for j in range(1, m+1):        # Q は P の転置
                tmp = q[j][i]*cost + q[j][i+1]*sint
                q[j][i+1] = -q[j][i]*sint + q[j][i+1]*cost
                q[j][i] = tmp
            
        # RQ の計算
        for i in range(1, m+1):
            for j in range(i, m+1):
                work[j] = a[i][j]
            for j in range(1, m+1):
                tmp = 0.0
                for k in range(i, m+1):
                    tmp += work[k] * q[k][j]
                a[i][j] = tmp
            
        # 原点移動後の処理
        for i in range(1, m+1):
            a[i][i] = a[i][i] + s


if __name__ == "__main__":
    main()            
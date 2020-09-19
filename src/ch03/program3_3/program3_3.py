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
    b = Dvector(1,N) # b[1...N]

    # ファイルのオープン
    with open("input_lu.dat", "r") as fin:
        with open("output_lu.dat", "w") as fout:
            input_matrix( a, 'A', fin, fout ) # 行列 A の入力
            input_vector( b, 'B', fin, fout ) # ベクトル b の入出力
            p = lu_decomp( a )                 # LU分解
            b = lu_solve( a, b, p )           # 前進代入・後退代入

            # 結果の出力
            fout.write("Ax=b の解は次の通りです\n")
            for i in range(1, N+1):
                fout.write(f"{b[i]}\n")


# LU分解
def lu_decomp(a: Dmatrix):
    eps = 2.0 ** -50.0 # eps = 2^{-50}とする
    p = [0] * (a.row_last_idx - a.row_head_idx + 1) # p[1...N-1] を利用, p[0] は未使用
    
    for k in range(1, N):
        # ピポットの選択
        amax = abs(a[k][k])
        ip = k
        for i in range(k+1, N+1):
            if abs(a[i][k]) > amax:
                amax = abs(a[i][k])
                ip = i
        
        # 正則性の判定
        if amax < eps:
            print("入力した行列は正則ではない!!")
        # ipを配列pに保存
        p[k] = ip
        # 行交換
        if ip != k:
            for j in range(k, N+1):
                tmp = a[k][j]
                a[k][j] = a[ip][j]
                a[ip][j] = tmp
        
        # 前進消去
        for i in range(k+1, N+1):
            alpha = - a[i][k] / a[k][k]
            a[i][k] = alpha
            for j in range(k+1, N+1):
                a[i][j] = a[i][j] + alpha * a[k][j]

    return p


# LU分解を利用して連立一次方程式を解く
def lu_solve(a: Dmatrix, b: Dvector, p):
    # 右辺の行交換
    for k in range(1, N):
        tmp = b[k]
        b[k] = b[p[k]]
        b[p[k]] = tmp
    # 前進代入
    for i in range(k+1, N+1):
        b[i] = b[i] + a[i][k] * b[k]

    # 後退代入
    b[N] = b[N] / a[N][N]
    for k in range(N-1, 0, -1):
        tmp = b[k]
        for j in range(k+1, N+1):
            tmp = tmp - a[k][j] * b[j]
        b[k] = tmp / a[k][k]
    
    return b


if __name__ == "__main__":
    main()
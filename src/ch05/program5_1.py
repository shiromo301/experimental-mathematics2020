import sys
sys.path.append("../ch02")

from program2_1 import Dvector
from program2_2 import Dmatrix
from program2_3 import input_vector, input_matrix
from program2_8 import vector_norm_max

N    = 10           # N元方程式
EPS  = 10.0 ** -8.0 # epsilon の設定
KMAX = 100          # 最大反復回数

def main():
    a = Dmatrix(1, N, 1, N) # 行列 a[1...N][1...N]
    b = Dvector(1, N)       # b[1...N]
    x = Dvector(1, N)       # x[1...N]

    # ファイルのオープン
    with open("input_sp.dat", "r") as fin:
        with open("output_sp.dat", "w") as fout:
            input_matrix( a, 'A', fin, fout ) # 行列 A の入出力
            input_vector( b, 'b', fin, fout ) # ベクトル b の入出力
            input_vector( x, 'x', fin, fout ) # 初期ベクトル x0 の入出力
            x = jacobi_lin( a, b, x )         # ヤコビ法

            # 結果の出力
            fout.write("Ax=b の解は次の通りです\n")
            for i in range(1, N+1):
                fout.write("{:.6f}\n".format(x[i]))


# ヤコビ法
def jacobi_lin(a: Dmatrix, b: Dvector, x: Dvector) -> Dvector:
    k = 0

    xn = Dvector(1, N) # xn[1...N]

    # x <- x_k, xn <- x_{k+1}
    while True:
        for i in range(1, N+1):
            xn[i] = b[i]
            for j in range(1, N+1):
                xn[i] -= a[i][j] * x[j]
            xn[i] += a[i][i] * x[i]  # 余分に引いた分を加える
            xn[i] /= a[i][i]
        for i in range(1, N+1):
            x[i] = xn[i] - x[i]
        eps = vector_norm_max(x)     # 最大値ノルムの計算
        for i in range(1, N+1):
            x[i] = xn[i]             # 値を更新
        k += 1

        if eps <= EPS or k >= KMAX:
            break
    
    if k == KMAX:
        print("答えが見つかりませんでした")
    else:
        print(f"反復回数は{k}回です")

    return x


if __name__ == "__main__":
    main()
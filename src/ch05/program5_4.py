import sys
sys.path.append("../ch02")

from program2_1 import Dvector
from program2_2 import Dmatrix
from program2_3 import input_vector, input_matrix
from program2_4 import inner_product
from program2_8 import vector_norm1

N    = 10           # N元方程式
EPS  = 10.0 ** -8.0 # epsilon の設定
KMAX = 100          # 最大反復回数

def main():
    global N

    a  = Dmatrix(1, N, 1, N) # 行列 a[1...N][1...N]
    b  = Dvector(1, N)       # b[1...N]
    x0 = Dvector(1, N)       # x[1...N]

    # ファイルのオープン
    with open("input_sp.dat", "r") as fin:
        with open("output_sp.dat", "w") as fout:
            input_matrix(  a,  'A', fin, fout ) # 行列 A の入出力
            input_vector(  b,  'b', fin, fout ) # ベクトル b の入出力
            input_vector( x0, 'x0', fin, fout ) # 初期ベクトル x0 の入出力
            x = cg( a, b, x0 )                  # 共役勾配法(CG法)

            # 結果の出力
            fout.write("Ax=b の解は次の通りです\n")
            for i in range(1, N+1):
                fout.write("{:.6f}\n".format(x[i]))


# 共役勾配法 (CG法)
def cg(a: Dmatrix, b: Dvector, x0: Dvector):
    k = 0

    r = Dvector(1, N) # r[1...N]
    p = Dvector(1, N) # p[1...N]
    x = x0.copy()

    tmp = matrix_vector_product( a, x ) # tmp <- A b

    for i in range(1, N+1):
        p[i] = b[i] - tmp[i]
        r[i] = p[i]

    while True:
        # alpha の計算
        tmp = matrix_vector_product( a, p ) # tmp <- A p_k
        work = inner_product(p, tmp)       # work <- (p, Ap_k)
        alpha = inner_product(p, r) / work

        # x_{k+1} と r_{k+1} の計算
        for i in range(1, N+1):
            x[i] += alpha * p[i]
        for i in range(1, N+1):
            r[i] -= alpha * tmp[i]

        # 収束判定
        eps = vector_norm1(r)
        k += 1 # 反復回数の更新
        if eps < EPS:
            break

        # beta と p_{k+1} の計算
        beta = - inner_product(r, tmp) / work
        for i in range(1, N+1):
            p[i] = r[i] + beta * p[i]

        if k >= KMAX:
            break

    if k == KMAX:
        print("答えが見つかりませんでした")
        exit(1)
    else:
        print(f"反復回数は{k}回です") # 反復回数を画面に表示
        return x


# 行列 a[1...N][1...N] と ベクトルb[1...N] との積
def matrix_vector_product(a: Dmatrix, b: Dvector):
    N = b.last_idx - b.head_idx + 1
    c = Dvector(1, N)

    for i in range(1, N+1):
        c[i] = sum( ( a[i][j] * b[j] for j in range(1, N+1) ) )

    return c


if __name__ == "__main__":
    main()
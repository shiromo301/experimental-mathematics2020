from program2_2 import Dmatrix

L = 3
M = 2
N = 3

def main():
    global L, M, N

    a = Dmatrix(1, L, 1, M) # 行列 a[1...L][1...M]
    b = Dmatrix(1, M, 1, N) # 行列 b[1...M][1...N]

    # 行列 A の定義
    for i in range(1, L+1):
       for j in range(1, M+1):
           a[i][j] = 2.0 * (i + j)

    # 行列 B の定義
    for i in range(1, M+1):
        for j in range(1, N+1):
            b[i][j] = 2.0 * (i + j)

    # 行列の積の計算
    c = matrix_product(a, b)
    # 結果の表示
    print("A x B の結果は次の通りです")
    for i in range(1, L+1):
        for j in range(1, N+1):
            print(c[i][j], end="  ")
        print()


def matrix_product(a: Dmatrix, b: Dmatrix) -> Dmatrix:
    l1, l2 = a.row_head_idx, a.row_last_idx
    m1, m2 = a.col_head_idx, a.col_last_idx
    n1, n2 = b.col_head_idx, b.col_last_idx
    c = Dmatrix(l1,l2,n1,n2)

    for i in range(l1, l2+1):         # 行の添字
        for j in range(n1, n2+1):
            c[i][j] = 0.0             # 変数の初期化
            for k in range(m1, m2+1): # 列の添字
                c[i][j] += a[i][k] * b[k][j]

    return c


if __name__ == "__main__":
    main()
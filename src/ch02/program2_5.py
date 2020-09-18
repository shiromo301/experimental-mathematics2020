from program2_2 import Dmatrix

ROW    = 3 # 行の要素数
COLUMN = 4 # 列の要素数

def main():
    global ROW, COLUMN
    a = Dmatrix(1, ROW, 1, COLUMN) # 行列 a[1...ROW][1...COLUMN]
    b = Dmatrix(1, ROW, 1, COLUMN) # 行列 b[1...ROW][1...COLUMN]

    # 行列の定義
    for i in range(1, ROW+1):
        for j in range(1, COLUMN+1):
            a[i][j] = 2.0 * (i + j)
            b[i][j] = 3.0 * (i + j)

    # 行列の和の計算
    c = matrix_sum(a, b)

    # 結果の表示
    print("行列 A と行列 B の和は次の通りです")
    for i in range(1, ROW+1):
        for j in range(1, COLUMN+1):
            print(c[i][j], end="  ")
        print()


# 行列の和
# a[m1...m2][n1...n2] と b[m1...m2][n1...n2] の和を求める.
def matrix_sum(a: Dmatrix, b: Dmatrix):
    m1, m2 = a.row_head_idx, a.row_last_idx
    n1, n2 = a.col_head_idx, a.col_last_idx
    c = Dmatrix(m1, m2, n1, n2)
    
    for i in range(m1, m2+1):
        for j in range(n1, n2+1):
            c[i][j] = a[i][j] + b[i][j]

    return c


if __name__ == "__main__":
    main()
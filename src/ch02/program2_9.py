from program2_1 import Dvector
from program2_2 import Dmatrix

ROW    = 3 # 行の要素数
COLUMN = 4 # 列の要素数

def main():
    global ROW, COLUMN

    a = Dmatrix(1, ROW, 1, COLUMN) # 行列 a[1...ROW][1...COLUMN]
    # 行列の定義
    print("A=")
    for i in range(1, ROW+1):
        for j in range(1, COLUMN+1):
            a[i][j] = 2.0 * (i + j) * (-1.0) ** j
            print(a[i][j], end="\t")
        print()

    print(f"Aの1ノルムは{matrix_norm1(a)}")
    print(f"Aの最大値ノルムは{matrix_norm_max(a)}")


# 1ノルムの計算
def matrix_norm1(a: Dmatrix):
    m1, m2 = a.row_head_idx, a.row_last_idx
    n1, n2 = a.col_head_idx, a.col_last_idx
    work = Dvector(n1, n2) # ベクトルwork[n1...n2]

    # 列和の計算
    for j in range(n1, n2+1):
        work[j] = 0.0
        for i in range(m1, m2+1):
            work[j] += abs(a[i][j])
    
    return max(work)


# 最大値ノルムの計算
def matrix_norm_max(a: Dmatrix):
    m1, m2 = a.row_head_idx, a.row_last_idx
    n1, n2 = a.col_head_idx, a.col_last_idx
    work = Dvector(m1, m2)

    # 行和の計算
    for i in range(m1, m2+1):
        work[i] = 0.0
        for j in range(n1, n2+1):
            work[i] += abs(a[i][j])

    return max(work)


if __name__ == "__main__":
    main()
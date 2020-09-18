import sys
sys.path.append("../ch02")

from program2_1 import Dvector
from program2_2 import Dmatrix
from program2_3 import input_vector

def main():
    print("データの個数を入力してください--->")
    n = int(input())
    n -= 1 # データ数がnなので, n <- n-1 として添え字を 0,1,...,n とする

    print("補間点を入力してください--->")
    xi = float(input())

    x = Dvector(0, n) # x[0...n]
    y = Dvector(0, n) # y[0...n]

    # ファイルのオープン
    with open("input_lag.dat", "r") as fin:
        with open("output_lag.dat", "w") as fout:
            input_vector( x, 'x', fin, fout ) # ベクトル x の入出力
            input_vector( y, 'y', fin, fout ) # ベクトル y の入出力

            print("補間の結果は, P({:.6f})={:.6f}".format(xi, newton_ip(x,y,n,xi)))

            # グラフを描くために結果をファイルに出力
            xi = x[0]
            while xi <= x[n]:
                fout.write("{:.6f} \t {:.6f}\n".format(xi, newton_ip(x,y,n,xi)))
                xi += 0.01
            

# ニュートン補間
# 添字は 0,1,...,n と仮定
def newton_ip(x: Dvector, y: Dvector, n: int, xi: float) -> float:
    pn = 0.0

    a = Dmatrix(0, n, 0, n)

    for i in range(n+1):
        a[i][0] = y[i]

    # 差商の計算
    for j in range(1, n+1):
        for i in range(n-j+1):
            a[i][j] = ( a[i+1][j-1] - a[i][j-1] ) / ( x[i+j] - x[i] )
    
    # 補間の計算
    pn, li = y[0], 1.0
    for j in range(1, n+1):
        li *= ( xi - x[j-1] )
        pn += a[0][j] * li

    return pn


if __name__ == "__main__":
    main()
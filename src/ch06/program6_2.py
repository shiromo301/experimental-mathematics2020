import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../ch02'))

from program2_1 import Dvector
from program2_3 import input_vector

def main():
    print("データの個数を入力してください--->")
    n = int(input())
    n -= 1 # データ数が n なので, n <- n-1 として添字を0,1,...,n とする

    print("補間点を入力してください--->")
    xi = float(input())

    x = Dvector(0, n) # x[0...n]
    y = Dvector(0, n) # y[0...n]

    # ファイルのオープン
    with open("input_lag.dat", "r") as fin:
        with open("output_lag.dat", "w") as fout:
            input_vector( x, "x", fin, fout ) # ベクトル x の入出力
            input_vector( y, "y", fin, fout ) # ベクトル y の入出力

            print("補間の結果は, P({:.6f})={:.6f}".format(xi, lagrange(x,y,0,n,xi)))

            # グラフを描くために結果をファイルに出力
            xi = x[0]
            while xi <= x[n]:
                fout.write("{:.6f} \t {:.6f}\n".format(xi, lagrange(x,y,0,n,xi)))
                xi += 0.01


# ラグランジュ補間
def lagrange(x: Dvector, y: Dvector, m: int, n: int, xi: float) -> float:
    pn = 0.0

    # P_n(x) の計算
    for i in range(m, n+1):
        li = 1.0
        # l_i(x) の計算
        for k in range(m, n+1):
            if k != i:
                li *= (xi - x[k]) / (x[i] - x[k])
        pn += li * y[i]
    return pn


if __name__ == "__main__":
    main()
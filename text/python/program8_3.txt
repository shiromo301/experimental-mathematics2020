import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../ch02'))

from program2_1 import Dvector
from program8_1 import func

def main():
    a, b, y0 = 0.0, 1.0, 1.0

    print("分割数を入力してください--->", end="")
    n = int(input())

    y = Dvector(0, n)
    y = rk4( y0, y, a, b, n, func ) # ルンゲクッタ法

    # 結果の表示
    h = (b - a) / n
    for i in range(n+1):
        print("x={:.6f} \t y={:.6f} ".format(a+i*h, y[i]))


# ルンゲ・クッタ法
def rk4(y0: float, y: Dvector, a: float, b: float, n: int, f ) -> Dvector:
    h = (b - a) / n
    # 初期値の設定
    y[0], x = y0, a

    # ルンゲ・クッタ法
    for i in range(n):
        k1 = f(x, y[i])
        k2 = f(x+h/2.0, y[i]+h*k1/2.0)
        k3 = f(x+h/2.0, y[i]+h*k2/2.0)
        k4 = f(x+h, y[i]+h*k3)
        y[i+1] = y[i] + h/6.0 * (k1 + 2.0*k2 + 2.0*k3 + k4)
        x += h

    return y


if __name__ == "__main__":
    main()
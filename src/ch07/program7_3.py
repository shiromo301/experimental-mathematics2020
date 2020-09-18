import sys
sys.path.append("../ch02")

from program2_1 import Dvector

def main():
    m = n = 20

    print("8x^2+4y を x=[1,2], y=[2-x,x^2] で積分します ")
    print("xの分割数は{}, yの分割数{}, 結果は{:15.10f}".format(
        m, n, trapezoidal2( 1.0, 2.0, m, n, phi, psi, func )
    ))


# 重積分用の台形公式
def trapezoidal2(a: float, b: float, m: int, n: int, p, q, f) -> float:
    F = Dvector(0, n)
    h = ( b - a ) / n         # 刻み幅の指定 (x 方向)

    # F_i の計算
    for i in range(n+1):
        x = a + i*h
        y1 = p(x)
        y2 = q(x)
        k = ( y2 - y1 ) / m   # 刻み幅の指定 (y 方向)
        F[i] = ( f(x, y1) + f(x, y2) ) / 2.0
        for j in range(1, m):
            F[i] += f(x, y1+j*k)
        F[i] *= k

    # 積分の計算
    T = ( F[0] + F[n] ) / 2.0
    for i in range(1, n):
        T += F[i]
    T *= h

    return T


# 被積分関数の定義
def func(x: float, y: float) -> float:
    return 8.0*x*x + 4.0*y


# y の積分区間
def phi(x: float):
    return 2.0 - x


def psi(x: float):
    return x*x

if __name__ == "__main__":
    main()
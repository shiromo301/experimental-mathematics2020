def main():
    n = 100

    print(f"2.0/(x*x) を [1,2] で積分します. 分割数は{n}です")
    print("結果は{:20.15f} です".format(trapezoidal(1.0, 2.0, n, func1)))

    print(f"4.0/(1+x*x) を [0,1] で積分します. 分割数は{n}です")
    print("結果は{:20.15f} です".format(trapezoidal(0.0, 1.0, n, func2)))


# 台形公式
def trapezoidal(a: float, b: float, n: int, f) -> float:
    h = ( b - a ) / n # 刻み幅の指定

    # 台形公式
    T = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        T += f(a + i*h)
    T *= h

    return T


# 関数の定義
def func1(x: float) -> float:
    return 2.0 / (x * x)


def func2(x: float) -> float:
    return 4.0 / (1.0 + x*x)


if __name__ == "__main__":
    main()
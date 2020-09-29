from program7_1 import func1, func2

def main():
    n = 50

    print(f"2.0/(x*x) を [1,2] で積分します. 分割数は{2*n}です")
    print("結果は{:20.15f} です".format(simpson(1.0, 2.0, n, func1)))

    print(f"4.0/(1+x*x) を [0, 1] で積分します. 分割数は{2*n}です")
    print("結果は{:20.15f} です".format(simpson(0.0, 1.0, n, func2)))


# シンプソン公式
def simpson(a: float, b: float, n: int, f) -> float:
    h = ( b - a ) / ( 2.0 * n ) # 刻み幅の指定

    # シンプソン公式
    S = f(a) + f(b)
    for i in range(1, n):
        S += 4.0*f( a + (2.0*i - 1.0)*h ) + 2.0*f( a + 2.0*i*h )
    S+= 4.0*f( a + (2.0*n-1.0)*h )
    S *= h / 3.0

    return S


if __name__ == "__main__":
    main()
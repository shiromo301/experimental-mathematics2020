from math import cos

EPS  = 10.0 ** -8.0 # epsilon の設定
NMAX = 100          # 最大反復回数

def main():
    print("初期値 x0 と x1 を入力してください")
    x0, x1 = map(float, input().split())

    secant( x0, x1 )


# 割線法
def secant(x0: float, x1: float):
    global EPS, NMAX
    n = 1
    d = x1 - x0
    y0 = f(x0)

    while True:
        y1 = f(x1)
        d = -d * y1 / (y1 - y0)
        x1 = x1 + d
        y0 = y1
        n += 1
        if abs(d) <= EPS or n >= NMAX:
            break

    if n == NMAX:
        print("答えが見つかりませんでした")
    else:
        print("答えは x={:.6f} です".format(x1))


def f(x: float) -> float:
    return x - cos(x)


if __name__ == "__main__":
    main()
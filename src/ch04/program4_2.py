from math import sin, cos

EPS = 10.0 ** -8.0 # epsilon の設定
NMAX = 10          # 最大反復回数

def main():
    print("初期値 x0 を入力してください")
    x = float(input())

    newton( x )


# Newton法
def newton(x: float):
    global EPS, NMAX
    n = 0

    while True:
        d = -f(x) / df(x)
        x = x + d
        n += 1
        if abs(d) <= EPS or n >= NMAX:
            break
    
    if n == NMAX:
        print("答えが見つかりませんでした")
    else:
        print(f"答えは x={x} です")


def f(x: float) -> float:
    return x - cos(x)


def df(x: float) -> float:
    return 1.0 + sin(x)


if __name__ == "__main__":
    main()

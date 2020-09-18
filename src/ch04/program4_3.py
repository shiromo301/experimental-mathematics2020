EPS  = 10.0 ** -8.0 # epsilon の設定
NMAX = 100          # 最大反復回数

def main():
    print("初期値 x0 を入力してください")
    x = float(input())

    newton1( x )


# Newton法 (重複次数つき)
def newton1(x: float):
    n = 0
    x0 = x1 = x2 = x # x で x0, x1, x2 を初期化

    while True:
        d = - f(x) / df(x)
        x = x + d
        n += 1
        x0 = x1
        x1 = x2
        x2 = x
        if abs(d) <= EPS or n >= NMAX:
            break

    m = (x0 - x1) / (x0 - 2.0*x1 + x2) # 重複次数の計算
    if n == NMAX:
        print("答えが見つかりませんでした")
    else:
        print("答えは x={:.6f} で, 重複次数は{:.6f}です".format(x, m))


# 関数の定義
def f(x: float) -> float:
    return (x*x*x) - (x*x) - x + 1.0


# 導関数の定義
def df(x: float) -> float:
    return (3.0*x*x) - (2.0*x) - 1.0


if __name__ == "__main__":
    main()
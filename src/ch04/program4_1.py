def main():
    eps = 2.0 ** -30.0

    print("初期区間 [a,b] を入力してください--->a b")
    a, b = map(float, input().split())
    print("区間の分割数 n を入力してください--->n")
    n = int(input())

    # 対象区間を探索しながら2分法を適用
    h = (b - a) / n
    y1 = f(a)
    x = a + h
    while x <= b:
        y2 = f(x)
        if y1 * y2 < 0.0:
            print("求める答えは x={:.6f} です".format(bisection(x-h, x, eps)))
        y1 = y2
        x += h


def bisection(a: float, b: float, eps: float):
    while True:
        c = (a + b) / 2.0
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        if abs(b - a) < eps:
            break

    c = (a + b) / 2.0

    return c


# 関数の定義
def f(x: float):
    return x ** 5 - 5 * (x ** 3) + 4 * x


if __name__ == "__main__":
    main()
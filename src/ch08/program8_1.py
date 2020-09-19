def main():
    print("分割数を入力してください--->", end="")
    n = int(input())

    euler( 0.0, 1.0, 0.0, 1.0, n, func )


# オイラー法
def euler(x: float, y: float, a: float, b: float, n: int, f):
    h = (b - a) / n # 刻み幅

    for _ in range(n):
        y = y + h * f(x,y)
        x += h
        print("x={:.6f} \t y={:.6f}".format(x, y))


# 関数の定義
def func(x: float, y: float) -> float:
    return x + y


if __name__ == "__main__":
    main()
from program8_1 import func

def main():
    print("分割数を入力してください--->", end="")
    n = int(input())

    heun( 0.0, 1.0, 0.0, 1.0, n, func)


# ホイン法
def heun(x: float, y: float, a: float, b: float, n: int, f):
    h = (b - a) / n

    for _ in range(n):
        k1 = f(x,y)
        k2 = f(x+h, y+h*k1)
        y = y + h/2.0 * ( k1 + k2 )
        x += h
        print("x={:.6f} \t y={:.6f} ".format(x, y))


if __name__ == "__main__":
    main()
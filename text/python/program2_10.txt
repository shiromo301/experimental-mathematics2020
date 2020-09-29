# 0.1をN回加えるプログラム

N = 1000000

def main():
    global N

    # Recursive summation
    s = 0.0
    for i in range(1, N+1):
        s += 0.1
    print("Recursive summation の結果は\t {:30.20f}".format(s))

    # Compensated summation
    s, e = 0.0, 0.0
    for i in range(1, N+1):
        tmp = s
        y = 0.1 + e
        s = tmp + y
        e = (tmp - s) + y
    print("Compensated summation の結果は\t {:30.20f}".format(s))


if __name__ == "__main__":
    main()
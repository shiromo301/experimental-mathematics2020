import numpy as np

def main():
    a = 0 / np.float32(0) # NaN の生成
    print(f"a={a} ")
    b = 1.0 + a           # NaN による演算
    print(f"b={b} ")


if __name__ == "__main__":
    main()
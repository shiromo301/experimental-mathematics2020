import numpy as np

def main():
    a = 1.0 / np.float32(0.0) # 無限大の生成
    print(f"a={a} ")
    b = 1.0 / a               # 無限大による除算
    print(f"b={b} ")


if __name__ == "__main__":
    main()
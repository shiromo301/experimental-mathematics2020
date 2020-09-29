import numpy as np

def main():
    a = 1.0 / np.float32(0.0)  # inf の生成
    b = -1.0 / np.float32(0.0) # -inf の生成
    print(f"a={a}, b={b} ")
    c, d = 1.0 / a, 1.0 / b                # 符号付きゼロの生成
    print(f"c={c}, d={d} ")
    print(f"ans1={1.0/c}, ans2={1.0/d}")


if __name__ == "__main__":
    main()
from program2_1 import Dvector

N = 5 # 要素数の指定

def main():
    global N

    # ベクトルの定義, 配列 a,b の添字は 1～N
    a, b = Dvector(1, N), Dvector(1, N)
    for i in range(1, N+1):
        a[i] = i / 20.0
        b[i] = i / 10.0

    print(f"a と b の内積は{inner_product(a, b)} です")


# ベクトルa[m...n] と b[m...n] の内積を計算する
def inner_product(a: Dvector, b: Dvector):
    s = 0.0

    for i,j in zip(a, b):
        s += i * j

    return s

if __name__ == "__main__":
    main()
from struct import pack, calcsize

def main():
    print("数字を入力してください--->")
    a = float(input())

    c = pack("d", a) # a の内容を配列 c にコピー

    print("sEEEEEEE EEEEdddd dddddddd... ")
    for i in range(calcsize("d")-1, -1, -1):
        for j in range(calcsize("c")*8-1, -1, -1):
            k = c[i] & (1 << j)          # j を 1 ずつずらして論理積を取る
            print(1 if k else 0, end="") # k=0 でなければ1, k=0 ならば 0 を表示
        print(" ", end="")
    print()


if __name__ == "__main__":
    main()
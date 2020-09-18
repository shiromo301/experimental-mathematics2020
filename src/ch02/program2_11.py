from random import randint, seed  # randint, seed 関数を使うのに必要

seed(0) # シードなしをシミュレートするために必要
RAND_MAX = 2147483647

def main():
    print("シードなし")
    for _ in range(2):
        print(rand(), end="\t")
    print()

    print("シードつき")
    seed()
    for _ in range(2):
        print(rand(), end="\t")
    print()


# C言語のrand関数に対応する関数
def rand():
    return randint(0, RAND_MAX)


if __name__ == "__main__":
    main()
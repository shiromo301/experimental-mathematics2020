N = 7

def main():
    global N
    a = [1.2, -2.3, -4.2, 5.5, 2.1, 7.2, 3.1]

    a.sort()

    for i in range(N):
        print(a[i])


if __name__ == "__main__":
    main()
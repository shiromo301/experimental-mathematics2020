N = 5

class Dvector(object):
    def __init__(self, head_idx: int, last_idx: int):
        self.head_idx = head_idx
        self.last_idx = last_idx
        self.vector = [0] * (last_idx - head_idx + 1)

    def __repr__(self):
        return str(self.vector)

    def __iter__(self):
        return iter(self.vector)

    def __getitem__(self, key: int):
        if not(self.head_idx <= key <= self.last_idx):
            raise IndexError("Index out of range")
        return self.vector[key - self.head_idx]
    
    def __setitem__(self, key: int, value):
        if not(self.head_idx <= key <= self.last_idx):
            raise IndexError("Index out of range")
        self.vector[key - self.head_idx] = value


def main():
    global N
    a = Dvector(1, N) # 配列 a の添字は 1～N
    b = Dvector(2, N+1) # 配列 b の添字は 2～N+1

    for i in range(1, N+1):
        a[i] = i / 20.0
        print(f"a[{i}] = {a[i]}")

    for i in range(2, N+2):
        b[i] = i / 20.0
        print(f"b[{i}] = {b[i]}")


if __name__ == "__main__":
    main()
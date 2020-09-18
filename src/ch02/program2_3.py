from program2_1 import Dvector
from program2_2 import Dmatrix

N = 4

def main():
    global N
    a = Dmatrix(1, N, 1, N) # 行列 a[1...N][1...N]
    b = Dvector(1, N) # b[1...N]
    with open("input.dat", "r") as fin:
        with open("output.dat", "w") as fout:
            input_matrix( a, 'A', fin, fout )
            input_vector( b, 'b', fin, fout )

# a[1...N][1...N] の入力
def input_matrix(a: Dmatrix, c: str, fin, fout):
    N = a.row_last_idx - a.row_head_idx + 1
    fout.write(f"行列{c}は次の通りです\n")
    for i in range(1, N+1):
        line = fin.readline().split()
        for j in range(1, N+1):
            a[i][j] = float(line[j-1])
            fout.write("{:5.2f}\t".format(a[i][j]))
        fout.write("\n")
    fin.readline()

# b[1...N] の入力
def input_vector(b: Dvector, c: str, fin, fout):
    N = b.last_idx - b.head_idx + 1
    fout.write(f"ベクトル{c}は次の通りです\n")
    line = fin.readline().split()
    for i in range(1, N+1):
        b[i] = float(line[i-1])
        fout.write("{:5.2f}\t\n".format(b[i]))
    fin.readline()


if __name__ == "__main__":
    main()
import numpy as np

def main():
    deps = np.float64(1.0) # マシンイプシロン (double 型)
    feps = np.float32(1.0) # マシンイプシロン (float  型)

    # double型のマシンイプシロンの計算
    # deps +1 > 1 の間, deps を 2 で割り続ける
    dtmp = deps + np.float64(1.0)
    while dtmp > 1:
        deps /= np.float64(2.0)
        dtmp = deps + np.float64(1.0)
    print("double 型の Machine epsilon は {:-16g}".format(2.0*deps))
    print("double 型の Unit roundoff は {:-16g}".format(deps))

    # float 型のマシンイプシロンの計算
    # feps + 1 > 1 の間, feps を 2 で割り続ける
    ftmp = feps + np.float32(1.0)
    while ftmp > 1:
        feps /= np.float32(2.0)
        ftmp = feps + np.float32(1.0)
    print("float 型の Machine epsilon は {:-16g}".format(2.0*feps))
    print("float 型の Unit roundoff は {:-16g}".format(feps))
    

if __name__ == "__main__":
    main()

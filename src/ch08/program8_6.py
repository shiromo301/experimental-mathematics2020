# TODO: バグ未修正のprogram3_4.pyにおける修正版コレスキー分解(cholesky_decomp)関数と
# 修正版コレスキー分解を利用して連立一次方程式を解く(cholesky_solve)関数を用いている
# ため, 先にprogram3_4.pyのバグを修正する必要あり.

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../ch02'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../ch03/program3_4'))

from program2_1 import Dvector
from program2_2 import Dmatrix
from program2_8 import vector_norm_max
from program3_4 import cholesky_decomp, cholesky_solve

def main():
    pass


if __name__ == "__main__":
    main()
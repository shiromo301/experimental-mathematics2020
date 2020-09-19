# TODO: program4_5同様, program3_3.pyがインポートできない問題を解決
# TODO: インポートが解決してもprogram3_3は現状LU分解を計算するlu_decomp関数及び
# LU分解を利用して連立一次方程式を解lu_solve関数のバグを修正しなければこのコード
# も正常に動作しない. 先にprogram3_3のバグを修正する

import sys
sys.path.append("../ch02")
sys.path.append("../ch03/program3_3")

from program2_1 import Dvector
from program2_2 import Dmatrix
from program2_4 import inner_product
from program3_3 import lu_decomp, lu_solve
from program9_2 import householder
from program9_3 import qr

N = 4

def main():
    pass


if __name__ == "__main__":
    main()
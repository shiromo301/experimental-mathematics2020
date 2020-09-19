def adds(x, y, z, N, DEG):
    up = 0
    for i in range(N, -1, -1):
        sum_ = x[i] + y[i] + up
        if sum_ > DEG - 1:
            z[i] = sum_ - DEG
            up   = 1
        else:
            z[i] = sum_
            up   = 0


def subs(x, y, z, N, DEG):
    borrow = 0
    for i in range(N, -1, -1):
        sub = x[i] - y[i] - borrow
        if sub >= 0:
            z[i] = sub
            borrow = 0
        else:
            z[i]   = DEG + sub
            borrow = 1
from math import factorial

def f(n):
    ret = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            ret.append(factorial(i))
        else:
            ret.append(i * (i + 1) // 2)
    return ret
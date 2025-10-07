def fizz_buzz(n):
    ns = [str(i) for i in range(n) if i % 11 == 0 or i % 13 == 0]
    s = ''.join(ns)
    return s.count('7')
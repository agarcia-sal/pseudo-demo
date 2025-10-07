def fizz_buzz(n):
    ns = [i for i in range(n) if i % 11 == 0 or i % 13 == 0]
    s = "".join(str(x) for x in ns)
    ans = sum(c == '7' for c in s)
    return ans
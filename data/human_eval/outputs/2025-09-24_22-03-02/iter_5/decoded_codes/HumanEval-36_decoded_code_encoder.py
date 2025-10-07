def fizz_buzz(n: int) -> int:
    ns = [i for i in range(n) if i % 11 == 0 or i % 13 == 0]
    s = ''.join(str(x) for x in ns)
    ans = sum(1 for c in s if c == '7')
    return ans
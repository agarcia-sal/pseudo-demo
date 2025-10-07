def fizz_buzz(n: int) -> int:
    ns = [i for i in range(n) if i % 11 == 0 or i % 13 == 0]
    s = ''.join(str(element) for element in ns)
    ans = sum(c == '7' for c in s)
    return ans
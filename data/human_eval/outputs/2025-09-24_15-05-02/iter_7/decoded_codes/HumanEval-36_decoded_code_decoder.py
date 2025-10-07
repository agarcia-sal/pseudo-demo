def fizz_buzz(n: int) -> int:
    ns = [i for i in range(n) if i % 11 == 0 or i % 13 == 0]
    s = ''.join(str(num) for num in ns)
    ans = sum(ch == '7' for ch in s)
    return ans
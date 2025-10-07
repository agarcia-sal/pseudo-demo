def fizz_buzz(n: int) -> int:
    ns = [i for i in range(n) if i % 11 == 0 or i % 13 == 0]
    list_of_strings = [str(x) for x in ns]
    s = ''.join(list_of_strings)
    ans = s.count('7')
    return ans
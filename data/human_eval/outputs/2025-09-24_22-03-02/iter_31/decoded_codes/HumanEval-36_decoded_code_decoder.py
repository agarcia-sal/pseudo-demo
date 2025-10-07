def fizz_buzz(n: int) -> int:
    ns = [i for i in range(n) if i % 11 == 0 or i % 13 == 0]
    string_list = [str(elem) for elem in ns]
    s = ''.join(string_list)
    ans = s.count('7')
    return ans
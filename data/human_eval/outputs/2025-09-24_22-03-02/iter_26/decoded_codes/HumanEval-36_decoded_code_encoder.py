def fizz_buzz(n: int) -> int:
    ns = []
    for i in range(n):
        condition_1 = i % 11 == 0
        condition_2 = i % 13 == 0
        if condition_1 or condition_2:
            ns.append(i)
    s = ''
    for index in range(len(ns)):
        element = ns[index]
        s += str(element)
    ans = 0
    for index in range(len(s)):
        c = s[index]
        if c == '7':
            ans += 1
    return ans
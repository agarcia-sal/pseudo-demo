def fizz_buzz(n: int) -> int:
    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''
    for j in range(len(ns)):
        s += str(ns[j])
    ans = 0
    for k in range(len(s)):
        if s[k] == '7':
            ans += 1
    return ans
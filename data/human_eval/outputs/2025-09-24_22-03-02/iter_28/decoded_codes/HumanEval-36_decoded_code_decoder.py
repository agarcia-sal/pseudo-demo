def fizz_buzz(n: int) -> int:
    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''
    for index in range(len(ns)):
        item = ns[index]
        str_item = str(item)
        s += str_item
    ans = 0
    for index in range(len(s)):
        c = s[index]
        if c == '7':
            ans += 1
    return ans
def fizz_buzz(n):
    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(str(x) for x in ns)
    ans = 0
    for character in s:
        ans += (character == '7')
    return ans
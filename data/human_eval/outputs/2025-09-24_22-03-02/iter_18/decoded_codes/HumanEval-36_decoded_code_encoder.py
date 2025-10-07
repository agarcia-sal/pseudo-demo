def fizz_buzz(n: int) -> int:
    ns = []
    i = 0
    while i < n:
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
        i += 1
    s = ""
    j = 0
    while j < len(ns):
        current_str = str(ns[j])
        s += current_str
        j += 1
    ans = 0
    k = 0
    while k < len(s):
        if s[k] == '7':
            ans += 1
        k += 1
    return ans
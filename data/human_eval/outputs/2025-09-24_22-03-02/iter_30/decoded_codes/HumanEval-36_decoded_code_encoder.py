def fizz_buzz(n: int) -> int:
    ns = []
    i = 0
    while i < n:
        condition1 = (i % 11 == 0)
        condition2 = (i % 13 == 0)
        if condition1 or condition2:
            ns.append(i)
        i += 1
    s = ""
    j = 0
    length_ns = len(ns)
    while j < length_ns:
        element_str = str(ns[j])
        s += element_str
        j += 1
    ans = 0
    k = 0
    length_s = len(s)
    while k < length_s:
        c = s[k]
        if c == '7':
            ans += 1
        k += 1
    return ans
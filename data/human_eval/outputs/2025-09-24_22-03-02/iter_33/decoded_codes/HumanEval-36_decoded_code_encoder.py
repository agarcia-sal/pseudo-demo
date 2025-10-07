def fizz_buzz(n: int) -> int:
    ns = []
    i = 0
    while i < n:
        mod_11 = i % 11
        mod_13 = i % 13
        if mod_11 == 0 or mod_13 == 0:
            ns.append(i)
        i += 1
    str_list = []
    j = 0
    while j < len(ns):
        str_element = str(ns[j])
        str_list.append(str_element)
        j += 1
    s = ''
    k = 0
    while k < len(str_list):
        s += str_list[k]
        k += 1
    ans = 0
    m = 0
    while m < len(s):
        c = s[m]
        if c == '7':
            ans += 1
        m += 1
    return ans
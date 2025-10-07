def fizz_buzz(n: int) -> int:
    ns = []
    i = 0
    while i < n:
        remainder_eleven = i % 11
        remainder_thirteen = i % 13
        if remainder_eleven == 0 or remainder_thirteen == 0:
            ns.append(i)
        i += 1
    string_list = []
    index_ns = 0
    while index_ns < len(ns):
        element = ns[index_ns]
        element_string = str(element)
        string_list.append(element_string)
        index_ns += 1
    s = ""
    index_sl = 0
    while index_sl < len(string_list):
        s += string_list[index_sl]
        index_sl += 1
    ans = 0
    index_s = 0
    while index_s < len(s):
        c = s[index_s]
        if c == '7':
            ans += 1
        index_s += 1
    return ans
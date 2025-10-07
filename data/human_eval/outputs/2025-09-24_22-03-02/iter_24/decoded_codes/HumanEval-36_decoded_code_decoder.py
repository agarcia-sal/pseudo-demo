def fizz_buzz(n: int) -> int:
    ns = []
    i = 0
    while i < n:
        mod_eleven = i % 11
        mod_thirteen = i % 13
        if mod_eleven == 0 or mod_thirteen == 0:
            ns.append(i)
        i += 1
    str_list = []
    index_to_ns = 0
    while index_to_ns < len(ns):
        current_number = ns[index_to_ns]
        current_str = str(current_number)
        str_list.append(current_str)
        index_to_ns += 1
    s = ''
    index_to_str_list = 0
    while index_to_str_list < len(str_list):
        s += str_list[index_to_str_list]
        index_to_str_list += 1
    ans = 0
    index_to_s = 0
    while index_to_s < len(s):
        c = s[index_to_s]
        if c == '7':
            ans += 1
        index_to_s += 1
    return ans
def fizz_buzz(n: int) -> int:
    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    string_list = []
    for j in range(len(ns)):
        current_element = ns[j]
        string_conversion = str(current_element)
        string_list.append(string_conversion)
    s = ''
    for k in range(len(string_list)):
        s += string_list[k]
    ans = 0
    for c_index in range(len(s)):
        if s[c_index] == '7':
            ans += 1
    return ans
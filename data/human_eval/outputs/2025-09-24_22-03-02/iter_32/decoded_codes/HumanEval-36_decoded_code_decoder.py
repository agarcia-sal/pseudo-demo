def fizz_buzz(n: int) -> int:
    ns = []
    for i in range(n):
        mod_eleven = i % 11
        mod_thirteen = i % 13
        if mod_eleven == 0 or mod_thirteen == 0:
            ns.append(i)
    string_list = []
    for j in range(len(ns)):
        element_string = str(ns[j])
        string_list.append(element_string)
    s = ""
    for k in range(len(string_list)):
        s += string_list[k]
    ans = 0
    for m in range(len(s)):
        if s[m] == '7':
            ans += 1
    return ans
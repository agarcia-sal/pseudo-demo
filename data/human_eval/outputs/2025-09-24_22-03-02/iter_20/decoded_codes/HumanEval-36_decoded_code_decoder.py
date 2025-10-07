from typing import List

def fizz_buzz(n: int) -> int:
    ns: List[int] = []
    i = 0
    while i < n:
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
        i += 1
    s = ''
    index = 0
    while index < len(ns):
        element = ns[index]
        element_string = str(element)
        s += element_string
        index += 1
    ans = 0
    index = 0
    while index < len(s):
        c = s[index]
        if c == '7':
            ans += 1
        index += 1
    return ans
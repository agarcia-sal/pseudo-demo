from typing import List

def fizz_buzz(n: int) -> int:
    ns: List[int] = []
    for i in range(n):
        if (i % 11 == 0) or (i % 13 == 0):
            ns.append(i)
    s = ""
    for index in range(len(ns)):
        s += str(ns[index])
    ans = 0
    for index in range(len(s)):
        if s[index] == '7':
            ans += 1
    return ans
from typing import List

def fizz_buzz(n: int) -> int:
    ns: List[int] = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s: str = ""
    for index in range(len(ns)):
        element = ns[index]
        s += str(element)
    ans: int = 0
    for index in range(len(s)):
        c = s[index]
        if c == '7':
            ans += 1
    return ans
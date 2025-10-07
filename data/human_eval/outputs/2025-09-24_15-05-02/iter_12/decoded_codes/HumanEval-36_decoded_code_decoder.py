from typing import List

def fizz_buzz(n: int) -> int:
    ns: List[int] = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(str(x) for x in ns)
    ans = 0
    for c in s:
        ans += (c == '7')
    return ans
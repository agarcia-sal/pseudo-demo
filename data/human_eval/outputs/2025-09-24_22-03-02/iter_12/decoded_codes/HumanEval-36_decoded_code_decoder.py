from typing import List

def fizz_buzz(n: int) -> int:
    ns: List[int] = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s: str = "".join(str(x) for x in ns)
    ans: int = 0
    for c in s:
        if c == '7':
            ans += 1
    return ans
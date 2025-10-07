from typing import List

def fizz_buzz(n: int) -> int:
    ns: List[int] = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(str(num) for num in ns)
    ans = sum(1 for c in s if c == '7')
    return ans
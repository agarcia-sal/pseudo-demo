from typing import List

def fizz_buzz(n: int) -> int:
    ns: List[int] = [i for i in range(n) if i % 11 == 0 or i % 13 == 0]
    s: str = ''.join(str(num) for num in ns)
    ans: int = sum(char == '7' for char in s)
    return ans
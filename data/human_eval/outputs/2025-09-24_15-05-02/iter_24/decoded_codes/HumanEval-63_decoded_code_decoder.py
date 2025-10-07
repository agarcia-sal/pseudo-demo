from typing import Dict

def fibfib(n: int, memo: Dict[int, int] = None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = 0
        return 0
    if n == 2:
        memo[n] = 1
        return 1
    memo[n] = fibfib(n - 1, memo) + fibfib(n - 2, memo) + fibfib(n - 3, memo)
    return memo[n]
def fibfib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1

    memo = {0: 0, 1: 0, 2: 1}

    def helper(k: int) -> int:
        if k in memo:
            return memo[k]
        memo[k] = helper(k - 1) + helper(k - 2) + helper(k - 3)
        return memo[k]

    return helper(n)
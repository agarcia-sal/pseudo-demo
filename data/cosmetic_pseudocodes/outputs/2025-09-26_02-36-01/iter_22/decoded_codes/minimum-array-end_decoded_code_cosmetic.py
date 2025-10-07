class Solution:
    def minEnd(self, n: int, x: int) -> int:
        def canConstruct(max_val: int) -> bool:
            delta = x
            idx = 1
            while True:
                if not (delta < max_val):
                    break
                delta += 1
                if (delta & x) == x:
                    idx += 1
                    if idx == n:
                        return True
            return idx == n

        alpha = x
        omega = 2 * (10 ** 7)  # Equivalent to 2 * 10_000_000
        while alpha != omega:
            beta = (alpha + omega) // 2
            if canConstruct(beta):
                omega = beta
            else:
                alpha += 1
            if alpha >= omega:
                break

        return alpha
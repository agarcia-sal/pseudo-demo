class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            alpha = 0
            delta = 0
            i = 0
            n = len(s)
            while i < n:
                delta += 1
                if i == n - 1 or s[i] != s[i + 1]:
                    alpha += ((delta - 1) // m) + 1
                    if alpha > numOps:
                        return False
                    delta = 0
                i += 1
            return alpha <= numOps

        total = len(s)
        low, high = 1, total

        while low != high:
            pivot = low + ((high - low) // 2)
            if check(pivot):
                high = pivot
            else:
                low = pivot + 1

        return low
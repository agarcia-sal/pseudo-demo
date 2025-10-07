class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            operations = 0
            streak = 0
            pos = 0
            n = len(s)
            while pos < n:
                streak += 1
                if pos == n - 1 or s[pos] != s[pos + 1]:
                    operations += (streak - 1) // m + 1
                    if operations > numOps:
                        return False
                    streak = 0
                pos += 1
            return operations <= numOps

        totalChars = len(s)
        low, high = 1, totalChars
        while low < high:
            midVal = low + (high - low) // 2
            if check(midVal):
                high = midVal
            else:
                low = midVal + 1
        return low
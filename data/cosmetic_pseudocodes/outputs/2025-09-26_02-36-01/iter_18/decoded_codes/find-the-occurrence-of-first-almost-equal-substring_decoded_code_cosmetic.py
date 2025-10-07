class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def is_almost_equal(x: str, y: str) -> bool:
            delta = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    delta += 1
                    if delta > 1:
                        return False
            return True

        n, m = len(s), len(pattern)
        start = 0
        output = -1
        while start <= n - m:
            if is_almost_equal(s[start:start + m], pattern):
                output = start
                break
            start += 1
        return output
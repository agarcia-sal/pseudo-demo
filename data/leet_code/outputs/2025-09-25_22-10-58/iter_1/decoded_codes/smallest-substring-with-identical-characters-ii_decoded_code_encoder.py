class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            cnt = 0
            k = 0
            for i, c in enumerate(s):
                k += 1
                if i == len(s) - 1 or c != s[i + 1]:
                    cnt += k // (m + 1)
                    if cnt > numOps:
                        return False
                    k = 0
            return cnt <= numOps

        n = len(s)
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
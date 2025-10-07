class Solution:
    def minEnd(self, n: int, x: int) -> int:
        def canConstruct(max_val: int) -> bool:
            current = x
            count = 1
            while current < max_val:
                current += 1
                if (current & x) == x:
                    count += 1
                    if count == n:
                        return True
            return count == n

        left = x
        right = 2 * 10**8  # 2 * 100,000,000 as per pseudocode's multiplication

        while left < right:
            mid = (left + right) // 2
            if canConstruct(mid):
                right = mid
            else:
                left += 1

        return left
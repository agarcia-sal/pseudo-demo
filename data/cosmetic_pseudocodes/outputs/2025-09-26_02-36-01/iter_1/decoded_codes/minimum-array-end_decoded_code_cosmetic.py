class Solution:
    def minEnd(self, n: int, x: int) -> int:
        def canConstruct(max_val: int) -> bool:
            temp = x
            found = 1
            while temp < max_val:
                temp += 1
                if (temp & x) == x:
                    found += 1
                    if found == n:
                        return True
            return found == n

        low = x
        high = 2 * 10**8
        while low < high:
            middle = (low + high) // 2
            if canConstruct(middle):
                high = middle
            else:
                low += 1
        return low
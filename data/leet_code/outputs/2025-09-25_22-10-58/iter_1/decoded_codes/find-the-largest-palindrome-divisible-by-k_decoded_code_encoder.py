class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if n == 1:
            for x in range(9, 0, -1):
                if x % k == 0:
                    return str(x)
            return "0"

        half = int("9" * ((n + 1) // 2))

        while half > 0:
            half_str = str(half)
            if n % 2 == 0:
                full = int(half_str + half_str[::-1])
            else:
                full = int(half_str + half_str[-2::-1])
            if full % k == 0:
                return str(full)
            half -= 1

        return "0"
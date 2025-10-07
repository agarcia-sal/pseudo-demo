class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if n == 1:
            r = 9
            while r >= 1:
                if r % k == 0:
                    return str(r)
                r -= 1
            return "0"

        m = (n + 1) // 2
        t = "9" * m
        p = int(t)

        while p > 0:
            s1 = str(p)
            if n % 2 == 0:
                s2 = s1[::-1]
                r = int(s1 + s2)
            else:
                s3 = s1[:-1][::-1]
                r = int(s1 + s3)
            if r % k == 0:
                return str(r)
            p -= 1

        return "0"
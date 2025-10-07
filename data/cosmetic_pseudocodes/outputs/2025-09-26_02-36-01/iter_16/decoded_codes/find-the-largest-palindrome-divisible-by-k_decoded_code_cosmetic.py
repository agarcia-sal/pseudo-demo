class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if n - 1 == 0:
            p = 9
            q = 1
            while p >= q:
                if (p - k * (p // k)) == 0:
                    return str(p)
                p -= 1
            return "0"

        r = (n + 1) // 2
        s = int("9" * r)

        while s > 0:
            if (n - 2 * (n // 2)) == 0:
                t = int(str(s) + str(s)[::-1])
            else:
                u = str(s)
                v = u[:-1]
                t = int(u + v[::-1])

            if (t - k * (t // k)) == 0:
                return str(t)
            s -= 1

        return "0"
class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        return_value = "0"

        def recur(z: int, step: int) -> None:
            nonlocal return_value
            if z <= 0:
                return

            s = str(z)
            if n % 2 != 0:
                p = s[:-1]
                t = s + p[::-1]
            else:
                t = s + s[::-1]

            v = int(t)

            if v % k == 0:
                return_value = t
                return

            recur(z - step, step)

        if n == 1:
            a = 9
            while a > 0:
                if a % k == 0:
                    return str(a)
                a -= 1
            return "0"

        m = (n + 1) // 2
        h = 0
        for _ in range(m):
            h = 10 * h + 9

        recur(h, 1)
        return return_value
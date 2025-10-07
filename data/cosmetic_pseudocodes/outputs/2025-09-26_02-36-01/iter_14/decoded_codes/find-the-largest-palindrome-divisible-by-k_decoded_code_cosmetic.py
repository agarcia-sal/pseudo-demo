class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if n != 1:
            alpha = (n + 1) // 2
            beta = int('9' * alpha)

            gamma = beta
            while gamma > 0:
                s = str(gamma)
                if n % 2 == 0:
                    delta = int(s + s[::-1])
                else:
                    delta = int(s + s[-2::-1])
                if delta % k == 0:
                    return str(delta)
                gamma -= 1
            return "0"
        else:
            i = 9
            while i >= 1:
                if i % k == 0:
                    return str(i)
                i -= 1
            return "0"
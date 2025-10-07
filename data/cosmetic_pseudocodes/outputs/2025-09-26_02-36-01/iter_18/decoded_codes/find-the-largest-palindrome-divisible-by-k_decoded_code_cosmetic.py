class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if n == 1:
            for i in range(9, 0, -1):
                if i % k == 0:
                    return str(i)
            return "0"

        alpha = (n + 1) // 2
        beta = "9" * alpha
        delta = int(beta)

        while delta >= 1:
            epsilon = str(delta)
            if n % 2 == 0:
                zeta = epsilon[::-1]
                palindromeVal = int(epsilon + zeta)
            else:
                temp = epsilon[:-1]
                zeta = temp[::-1]
                palindromeVal = int(epsilon + zeta)

            if palindromeVal % k == 0:
                return str(palindromeVal)
            delta -= 1

        return "0"
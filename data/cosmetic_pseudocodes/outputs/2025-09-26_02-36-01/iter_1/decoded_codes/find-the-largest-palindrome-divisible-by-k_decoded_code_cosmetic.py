class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if n == 1:
            candidate = 9
            while candidate >= 1:
                if candidate % k == 0:
                    return str(candidate)
                candidate -= 1
            return "0"

        halfLength = (n + 1) // 2
        half = int("9" * halfLength)

        while half > 0:
            halfStr = str(half)
            if n % 2 == 0:
                mirrored = halfStr + halfStr[::-1]
            else:
                mirrored = halfStr + halfStr[-2::-1]

            fullNumber = int(mirrored)
            if fullNumber % k == 0:
                return mirrored

            half -= 1

        return "0"
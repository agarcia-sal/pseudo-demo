class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if n == 1:
            digit = 9
            while digit > 0:
                if digit % k == 0:
                    return str(digit)
                digit -= 1
            return "0"

        halfLength = (n + 1) // 2
        nineStr = "9" * halfLength
        half = int(nineStr)

        while half > 0:
            halfStr = str(half)
            if n % 2 == 0:
                reversedHalf = halfStr[::-1]  # reverse entire halfStr
                fullStr = halfStr + reversedHalf
            else:
                reversedHalfSub = halfStr[:-1][::-1]  # reverse halfStr excluding last char
                fullStr = halfStr + reversedHalfSub

            full = int(fullStr)
            if full % k == 0:
                return fullStr
            half -= 1

        return "0"
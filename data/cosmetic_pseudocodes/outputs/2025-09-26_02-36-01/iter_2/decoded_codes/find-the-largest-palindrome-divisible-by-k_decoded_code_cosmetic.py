class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if n == 1:
            digitVar = 9
            while digitVar >= 1:
                if digitVar % k == 0:
                    return str(digitVar)
                digitVar -= 1
            return "0"

        halfLen = (n + 1) // 2
        nineStr = "9" * halfLen
        halfVal = int(nineStr)

        while halfVal > 0:
            halfStr = str(halfVal)
            if n % 2 == 0:
                fullStr = halfStr + halfStr[::-1]
            else:
                fullStr = halfStr + halfStr[:-1][::-1]
            fullNum = int(fullStr)
            if fullNum % k == 0:
                return fullStr
            halfVal -= 1

        return "0"
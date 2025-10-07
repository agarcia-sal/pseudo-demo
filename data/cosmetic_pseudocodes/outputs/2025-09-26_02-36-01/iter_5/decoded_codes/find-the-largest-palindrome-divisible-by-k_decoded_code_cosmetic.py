class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        def recSearch(current: int) -> str:
            if current < 1:
                return "0"

            isEven = (n % 2 == 0)
            leftPart = str(current)
            rightPart = ""

            if isEven:
                idxEnd = len(leftPart)
                idxStart = 1
            else:
                idxEnd = len(leftPart) - 1
                idxStart = 1

            for pos in range(idxEnd, idxStart - 1, -1):
                rightPart += leftPart[pos - 1]

            palindromeNum = int(leftPart + rightPart)
            if palindromeNum % k == 0:
                return str(palindromeNum)
            else:
                return recSearch(current - 1)

        if n == 1:
            digit = 9
            while digit >= 1:
                if digit % k == 0:
                    return str(digit)
                digit -= 1
            return "0"

        halfLen = (n + 1) // 2
        startHalfStr = "9" * halfLen
        startHalf = int(startHalfStr)

        return recSearch(startHalf)
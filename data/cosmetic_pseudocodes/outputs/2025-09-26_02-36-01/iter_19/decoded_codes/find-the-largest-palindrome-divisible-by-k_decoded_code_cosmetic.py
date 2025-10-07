class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if n == 1:
            candidate = 9
            while candidate >= 1:
                if candidate % k == 0:
                    return str(candidate)
                candidate -= 1
            return "0"

        halfDigitCount = (n + 1) // 2
        halfStr = "9" * halfDigitCount
        halfVal = int(halfStr)

        def buildPalindrome(seg: int, length: int) -> int:
            segStr = str(seg)
            if length % 2 == 0:
                return int(segStr + segStr[::-1])
            else:
                return int(segStr + segStr[-2::-1])  # reverse excluding last char

        currentHalf = halfVal
        while currentHalf > 0:
            candidateVal = buildPalindrome(currentHalf, n)
            if candidateVal % k == 0:
                return str(candidateVal)
            currentHalf -= 1

        return "0"
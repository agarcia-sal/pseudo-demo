class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        result = "0"

        if (n - 1) == 0:
            counter = 9
            while counter >= 1:
                if counter % k == 0:
                    result = str(counter)
                    break
                counter -= 1
            return result

        def toNumericStringRepeat(times: int) -> str:
            return "9" * times

        def reverseString(s: str) -> str:
            return s[::-1]

        halfLen = (n + 1) // 2
        prefixNum = int(toNumericStringRepeat(halfLen))

        def makeFullNumber(prefix: int, lengthEven: bool) -> int:
            prefixStr = str(prefix)
            if lengthEven:
                return int(prefixStr + reverseString(prefixStr))
            else:
                truncatedPrefix = prefixStr[:-1]
                return int(prefixStr + reverseString(truncatedPrefix))

        candidate = prefixNum
        while candidate > 0:
            palindromeVal = makeFullNumber(candidate, (n % 2 == 0))
            if palindromeVal % k == 0:
                result = str(palindromeVal)
                break
            candidate -= 1

        return result
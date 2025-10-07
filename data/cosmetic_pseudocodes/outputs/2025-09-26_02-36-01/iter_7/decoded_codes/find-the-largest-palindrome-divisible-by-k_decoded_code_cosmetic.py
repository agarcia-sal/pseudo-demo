class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        ZERO_STR = "0"
        ONE_INT = 1
        NINE_INT = 9
        TWO_INT = 2

        def toString(num: int) -> str:
            return str(num)

        def toInt(s: str) -> int:
            return int(s)

        def reverseString(s: str) -> str:
            # Efficient reversal using Python slicing
            return s[::-1]

        def substring(s: str, startPos: int, endPos: int) -> str:
            return s[startPos:endPos]

        def concatStrings(a: str, b: str) -> str:
            return a + b

        if n == ONE_INT:
            y = NINE_INT
            while y >= ONE_INT:
                if y % k == 0:
                    return toString(y)
                y -= ONE_INT
            return ZERO_STR
        else:
            halfLen = (n + ONE_INT) // TWO_INT
            halfStr = "".join(toString(NINE_INT) for _ in range(halfLen))
            halfVal = toInt(halfStr)

            def buildPalindrome(hVal: int) -> int:
                hs = toString(hVal)
                if n % TWO_INT == 0:
                    reversedHs = reverseString(hs)
                    return toInt(concatStrings(hs, reversedHs))
                else:
                    subStr = substring(hs, 0, len(hs) - ONE_INT)
                    reversedSub = reverseString(subStr)
                    return toInt(concatStrings(hs, reversedSub))

            def loop(hVal: int) -> str:
                if hVal < 0:
                    return ZERO_STR
                candidate = buildPalindrome(hVal)
                if candidate % k == 0:
                    return toString(candidate)
                return loop(hVal - ONE_INT)

            return loop(halfVal)
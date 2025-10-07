class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        def toString(num: int) -> str:
            return str(num)

        def stringReverse(s: str) -> str:
            def helper(idx: int, acc: str) -> str:
                if idx < 0:
                    return acc
                return helper(idx - 1, acc + s[idx])
            return helper(len(s) - 1, "")

        def substring(s: str, startIdx: int, endIdx: int) -> str:
            def subHelper(i: int, acc: str) -> str:
                if i == endIdx:
                    return acc
                return subHelper(i + 1, acc + s[i])
            return subHelper(startIdx, "")

        def digitNineRepeated(times: int) -> str:
            def repeatHelper(count: int, acc: str) -> str:
                if count == 0:
                    return acc
                return repeatHelper(count - 1, acc + "9")
            return repeatHelper(times, "")

        def toInt(s: str) -> int:
            def toIntHelper(i: int, length: int, result: int) -> int:
                if i == length:
                    return result
                digitVal = ord(s[i]) - ord('0')
                return toIntHelper(i + 1, length, result * 10 + digitVal)
            return toIntHelper(0, len(s), 0)

        def isDivisibleBy(value: int, divisor: int) -> bool:
            return (value - ((value // divisor) * divisor)) == 0

        if (n - 1) == 0:
            def descendLoop(x: int) -> str:
                if x < 1:
                    return "0"
                if isDivisibleBy(x, k):
                    return toString(x)
                else:
                    return descendLoop(x - 1)
            return descendLoop(9)

        halfCount = (n + 1) // 2
        nineString = digitNineRepeated(halfCount)
        half = toInt(nineString)

        def palindromeCheck(currHalf: int) -> str:
            if currHalf <= 0:
                return "0"
            halfStr = toString(currHalf)
            leftPart = halfStr
            if isDivisibleBy(n, 2):
                rightPart = stringReverse(halfStr)
            else:
                rightPart = stringReverse(substring(halfStr, 0, len(halfStr) - 1))
            fullStr = leftPart + rightPart
            fullNum = toInt(fullStr)
            if isDivisibleBy(fullNum, k):
                return fullStr
            else:
                return palindromeCheck(currHalf - 1)

        return palindromeCheck(half)
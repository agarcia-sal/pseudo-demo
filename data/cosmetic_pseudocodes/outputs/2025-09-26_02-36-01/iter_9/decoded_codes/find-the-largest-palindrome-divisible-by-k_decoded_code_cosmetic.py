class Solution:
    def largestPalindrome(self, beta: int, gamma: int) -> str:
        def IsDivisible(delta: int, epsilon: int) -> bool:
            return delta % epsilon == 0

        def ToString(val: int) -> str:
            return str(val)

        def RepeatChar(char: str, count: int) -> str:
            return char * count

        if beta == 1:
            u = 9
            while u >= 1:
                if IsDivisible(u, gamma):
                    return ToString(u)
                u -= 1
            return ToString(0)

        def IntFromString(s: str) -> int:
            return int(s)

        halfLength = (beta + 1) // 2
        halfStr = RepeatChar("9", halfLength)
        halfInt = IntFromString(halfStr)

        def ReverseString(ss: str) -> str:
            return ss[::-1]

        while halfInt > 0:
            halfStrRepr = ToString(halfInt)
            if (beta - 2 * (beta // 2)) == 0:
                concatStr = halfStrRepr + ReverseString(halfStrRepr)
            else:
                truncSubstr = halfStrRepr[:-1]
                concatStr = halfStrRepr + ReverseString(truncSubstr)
            candidate = IntFromString(concatStr)
            if IsDivisible(candidate, gamma):
                return ToString(candidate)
            halfInt -= 1

        return ToString(0)
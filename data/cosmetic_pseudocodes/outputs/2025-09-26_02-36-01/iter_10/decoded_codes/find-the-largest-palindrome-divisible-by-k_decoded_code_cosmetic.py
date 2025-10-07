class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        def IsDivisibleBy(num: int, denom: int) -> bool:
            return num % denom == 0

        def ToStringRev(s: str) -> str:
            revString = ""
            i = len(s) - 1
            while i >= 0:
                revString += s[i]
                i -= 1
            return revString

        def SubstringExclLast(s: str) -> str:
            return s[:len(s) - 1]

        def ConcatStr(a: str, b: str) -> str:
            return a + b

        def IntFromStr(s: str) -> int:
            return int(s)

        def NineRepeated(count: int) -> str:
            result = ""
            z = 0
            while z < count:
                result += "9"
                z += 1
            return result

        if n == 1:
            y = 9
            while y > 0:
                if IsDivisibleBy(y, k):
                    return str(y)
                y -= 1
            return "0"
        else:
            halfIter = IntFromStr(NineRepeated(((n + 1) // 2)))

            def DecrementHalf():
                nonlocal halfIter
                halfIter -= 1

            while halfIter > 0:
                halfStr = str(halfIter)
                palindromeNum = 0
                if (n % 2) == 0:
                    palindromeNum = IntFromStr(ConcatStr(halfStr, ToStringRev(halfStr)))
                else:
                    palindromeNum = IntFromStr(ConcatStr(halfStr, ToStringRev(SubstringExclLast(halfStr))))

                if IsDivisibleBy(palindromeNum, k):
                    return str(palindromeNum)

                DecrementHalf()

            return "0"
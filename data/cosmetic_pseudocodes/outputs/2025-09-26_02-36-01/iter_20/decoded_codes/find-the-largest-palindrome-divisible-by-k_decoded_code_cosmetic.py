class ReturnException(Exception):
    def __init__(self, val):
        self.val = val

class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        def customToString(v: int) -> str:
            if v == 0:
                return "0"
            c = []
            m = v
            while m > 0:
                r = m - (m // 10) * 10
                m = m // 10
                c.append(chr(48 + r))
            return ''.join(reversed(c))

        def customReverse(s: str) -> str:
            t = []
            i = len(s) - 1
            while i >= 0:
                t.append(s[i])
                i -= 1
            return ''.join(t)

        def concatStrings(a: str, b: str) -> str:
            # Efficient concatenation by direct join
            return a + b

        def toInteger(s: str) -> int:
            val = 0
            for ch in s:
                val = val * 10 + (ord(ch) - 48)
            return val

        if n == 1:
            u = 9
            def loopDescending():
                nonlocal u
                if u < 1:
                    return
                if (u % k) == 0:
                    vResult = customToString(u)
                    raise ReturnException(vResult)
                u -= 1
                loopDescending()
            try:
                loopDescending()
            except ReturnException as e:
                return e.val
            return "0"

        halfStr = ""
        halfCount = (n + 1) // 2
        i1 = 0
        while i1 < halfCount:
            halfStr += "9"
            i1 += 1

        halfNum = toInteger(halfStr)

        def descendHalf():
            nonlocal halfNum
            if halfNum <= 0:
                return

            halfStrLocal = customToString(halfNum)

            if (n % 2) == 0:
                revHalf = customReverse(halfStrLocal)
                fullStr = concatStrings(halfStrLocal, revHalf)
                fullNum = toInteger(fullStr)
            else:
                truncated = ""
                idx2 = 0
                while idx2 < len(halfStrLocal) - 1:
                    truncated += halfStrLocal[idx2]
                    idx2 += 1
                revTrunc = customReverse(truncated)
                fullStr = concatStrings(halfStrLocal, revTrunc)
                fullNum = toInteger(fullStr)

            if (fullNum % k) == 0:
                raise ReturnException(customToString(fullNum))

            halfNum -= 1
            descendHalf()

        try:
            descendHalf()
        except ReturnException as e:
            return e.val

        return "0"
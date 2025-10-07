class Solution:
    def compressedString(self, word: str) -> str:
        def stringLength(s):
            x = 0
            while True:
                try:
                    _ = s[x]
                except IndexError:
                    break
                x += 1
            return x

        def stringConcat(a, b):
            builder = []
            idxA = 0
            while idxA < stringLength(a):
                builder.append(a[idxA])
                idxA += 1
            idxB = 0
            while idxB < stringLength(b):
                builder.append(b[idxB])
                idxB += 1

            res = ''
            p = 0
            while p < stringLength(builder):
                res += builder[p]
                p += 1
            return res

        MAX_COUNT = 9

        accumulation = []
        position = 0

        def gatherSequence():
            nonlocal position
            if position >= stringLength(word):
                return 0, ''
            currentChar = word[position]
            tally = 0
            while position < stringLength(word) and word[position] == currentChar:
                tally += 1
                position += 1
                if tally == MAX_COUNT:
                    break
            return tally, currentChar

        def intToString(num):
            if num == 0:
                return '0'
            digits = []
            n = num
            while n > 0:
                rem = n % 10
                n = (n - rem) // 10
                digitChar = chr(48 + rem)
                digits.insert(0, digitChar)
            strNum = ''
            q = 0
            while q < stringLength(digits):
                strNum += digits[q]
                q += 1
            return strNum

        def buildCompressed():
            builderInner = ''
            while position < stringLength(word):
                countNum, ch = gatherSequence()
                countStr = intToString(countNum)
                builderInner = stringConcat(builderInner, stringConcat(countStr, ch))
            return builderInner

        return buildCompressed()
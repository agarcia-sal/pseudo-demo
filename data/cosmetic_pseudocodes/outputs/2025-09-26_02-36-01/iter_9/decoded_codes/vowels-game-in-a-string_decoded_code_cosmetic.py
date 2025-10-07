class Solution:
    def doesAliceWin(self, p: str) -> bool:
        def isVowel(x: str) -> bool:
            return x in ('a', 'e', 'i', 'o', 'u')

        def countTotalVowels(seq: str) -> int:
            y = 0
            idx = 0
            while idx < len(seq):
                if isVowel(seq[idx]):
                    y += 1
                idx += 1
            return y

        def processSegments(s: str) -> int:
            countSeg = 0
            currCount = 0
            oddFlag = False

            def mod2EqualsOne(val: int) -> bool:
                return (val % 2) == 1

            pos = 0
            while pos < len(s):
                c = s[pos]
                if isVowel(c):
                    oddFlag = not oddFlag
                if not oddFlag and mod2EqualsOne(currCount):
                    countSeg += 1
                    currCount = 0
                elif oddFlag:
                    currCount += 1
                pos += 1

            if oddFlag and mod2EqualsOne(currCount):
                countSeg += 1

            return countSeg

        def oddIsOne(n: int) -> bool:
            return (n % 2) == 1

        j = 0
        q = 0
        r = 0
        t = False

        q = countTotalVowels(p)
        r = processSegments(p)
        return oddIsOne(r)
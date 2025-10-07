class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowelsSet = {'a', 'e', 'i', 'o', 'u'}
        oddSegmentCounter = 0
        countCurrentVowels = 0

        def countVowels(index: int) -> int:
            if index > len(s):
                return 0
            ch = s[index - 1]
            increment = 1 if ch in vowelsSet else 0
            return increment + countVowels(index + 1)

        countCurrentVowels = countVowels(1)

        flagInOddSegment = False

        def iterateChars(i: int):
            nonlocal oddSegmentCounter, countCurrentVowels, flagInOddSegment
            if i > len(s):
                return
            currentChar = s[i - 1]
            if currentChar in vowelsSet:
                flagInOddSegment = not flagInOddSegment
            if not flagInOddSegment and countCurrentVowels % 2 == 1:
                oddSegmentCounter += 1
                countCurrentVowels = 0
            elif flagInOddSegment:
                countCurrentVowels += 1
            iterateChars(i + 1)

        iterateChars(1)

        if flagInOddSegment and countCurrentVowels % 2 == 1:
            oddSegmentCounter += 1

        resultFlag = (oddSegmentCounter % 2 == 1)
        return resultFlag
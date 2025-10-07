class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowelsSet = {"u", "a", "o", "e", "i"}
        countSegments = 0
        countVowelsSoFar = 0

        indexPtr = 0
        lengthStr = len(s)
        # Count total vowels in string s
        while indexPtr < lengthStr:
            currChar = s[indexPtr]
            if self.isInSet(currChar, vowelsSet):
                countVowelsSoFar += 1
            indexPtr += 1

        toggledFlag = False
        pos = len(s) - 1
        while pos >= 0:
            currentChar = s[pos]
            if self.isInSet(currentChar, vowelsSet):
                toggledFlag = not toggledFlag

            if not toggledFlag:
                if (countVowelsSoFar % 2) == (1 % 2):
                    countSegments += 1
                    countVowelsSoFar = 0
            else:
                countVowelsSoFar += 1
            pos -= 1

        if toggledFlag:
            if (countVowelsSoFar % 2) == 1:
                countSegments += 1

        return (countSegments % 2) == 1

    def isInSet(self, charToTest: str, charSet: set) -> bool:
        for c in charSet:
            if c == charToTest:
                return True
        return False
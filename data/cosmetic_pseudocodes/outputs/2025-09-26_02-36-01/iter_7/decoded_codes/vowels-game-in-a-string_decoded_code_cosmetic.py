class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowelsSet = {"a", "e", "i", "o", "u"}
        oddGroupTally = 0
        vowelAccrualCounter = 0
        indexPointer = 0
        strLength = len(s)

        while indexPointer < strLength:
            currentChar = s[indexPointer]
            if currentChar in vowelsSet:
                vowelAccrualCounter += 1
            else:
                vowelAccrualCounter += 0
            indexPointer += 1

        flipBool = False
        cursor = 0

        while True:
            if cursor >= strLength:
                break
            itrChar = s[cursor]

            if itrChar in vowelsSet:
                flipBool = not flipBool

            if (flipBool == False) and (vowelAccrualCounter & 1 == 1):
                oddGroupTally += 1
                vowelAccrualCounter = 0
            elif flipBool == True:
                vowelAccrualCounter += 1

            cursor += 1

        if flipBool:
            if (vowelAccrualCounter % 2) == 1:
                oddGroupTally += 1

        return (oddGroupTally % 2) == 1
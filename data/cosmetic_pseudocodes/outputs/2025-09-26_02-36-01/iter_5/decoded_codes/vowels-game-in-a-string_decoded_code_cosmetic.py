class Solution:
    def doesAliceWin(self, inputString: str) -> bool:
        vowelsSet = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}

        def countVowelsRec(index: int, accumulatedCount: int) -> int:
            if index >= len(inputString):
                return accumulatedCount
            currentChar = inputString[index]
            incrementedCount = accumulatedCount
            if currentChar in vowelsSet:
                incrementedCount = accumulatedCount + 1
            return countVowelsRec(index + 1, incrementedCount)

        totalVowels = countVowelsRec(0, 0)

        def processSegmentsRec(pos: int, vowelCountState: int, oddSegmentsAcc: int, oddSegmentFlag: bool) -> int:
            if pos >= len(inputString):
                if oddSegmentFlag and (vowelCountState % 2 != 0):
                    oddSegmentsAcc += 1
                return oddSegmentsAcc
            currentCharacter = inputString[pos]

            flagAfterToggle = oddSegmentFlag
            if currentCharacter in vowelsSet:
                flagAfterToggle = not oddSegmentFlag

            if (not oddSegmentFlag) and (vowelCountState % 2 == 1):
                newOddSegmentsAcc = oddSegmentsAcc + 1
                newVowelCountState = 0
                return processSegmentsRec(pos + 1, newVowelCountState, newOddSegmentsAcc, flagAfterToggle)
            elif oddSegmentFlag:
                return processSegmentsRec(pos + 1, vowelCountState + 1, oddSegmentsAcc, flagAfterToggle)
            else:
                return processSegmentsRec(pos + 1, vowelCountState, oddSegmentsAcc, flagAfterToggle)

        resultSegments = processSegmentsRec(0, totalVowels, 0, False)

        finalOutcome = (resultSegments % 2) == 1
        return finalOutcome
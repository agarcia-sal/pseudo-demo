class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowelsSet = {"o", "a", "u", "i", "e"}

        def equalsAny(ch, set_):
            for idx in range(len(set_)):
                # As set_ is a set, iterate over list of elements to simulate original logic
                # But since sets have no order, convert to list here
                if list(set_)[idx] == ch:
                    return True
            return False

        def lengthOf(arr):
            count = 0
            while count < len(arr):
                count += 1
            return count

        def containVowel(c):
            return equalsAny(c, vowelsSet)

        def scanVowels(arrayStr, index, total):
            if index >= lengthOf(arrayStr):
                return total
            else:
                charac = arrayStr[index]
                increment = 1 if containVowel(charac) else 0
                return scanVowels(arrayStr, index + 1, total + increment)

        accCount = scanVowels(s, 0, 0)

        toggleState = False
        segmentCounter = 0
        tempCount = accCount

        def processSegments(inputStr, position, state, count, segments):
            if position >= lengthOf(inputStr):
                if state:
                    rem = count % 2
                    if rem == 1:
                        return segments + 1
                    else:
                        return segments
                else:
                    return segments
            else:
                currentChar = inputStr[position]
                newState = state
                ifVowel = containVowel(currentChar)
                if ifVowel:
                    newState = not state

                updatedSegments = segments
                updatedCount = count

                if (newState == False) and ((count % 2) == 1):
                    updatedSegments = segments + 1
                    updatedCount = 0
                elif newState == True:
                    updatedCount = count + 1

                return processSegments(inputStr, position + 1, newState, updatedCount, updatedSegments)

        segmentCounter = processSegments(s, 0, toggleState, tempCount, 0)

        return (segmentCounter % 2) == 1
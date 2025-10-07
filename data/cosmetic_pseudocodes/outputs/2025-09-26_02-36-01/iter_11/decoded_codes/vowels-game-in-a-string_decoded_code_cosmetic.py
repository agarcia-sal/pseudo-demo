class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowelsSet = {'u', 'i', 'e', 'a', 'o'}

        def isVowel(x: str) -> bool:
            return x in vowelsSet

        def countOddParitySegments(sequence: str) -> int:
            class Flag:
                def __init__(self):
                    self.value = False

            flagObject = Flag()

            def toggleFlag(flagRef: Flag) -> None:
                flagRef.value = not flagRef.value

            def countVowels(idx: int, acc: int) -> int:
                if idx >= len(sequence):
                    return acc
                currentChar = sequence[idx]
                return countVowels(idx + 1, acc + (1 if isVowel(currentChar) else 0))

            countTracker = countVowels(0, 0)

            def segmentCounter(pos: int, oddSegCount: int, currentCount: int) -> int:
                if pos >= len(sequence):
                    return oddSegCount + (1 if flagObject.value and (currentCount % 2 == 1) else 0)
                character = sequence[pos]
                if isVowel(character):
                    toggleFlag(flagObject)
                if not flagObject.value and (currentCount % 2 == 1):
                    return segmentCounter(pos + 1, oddSegCount + 1, 0)
                elif flagObject.value:
                    return segmentCounter(pos + 1, oddSegCount, currentCount + 1)
                else:
                    return segmentCounter(pos + 1, oddSegCount, currentCount)

            return segmentCounter(0, 0, countTracker)

        result = countOddParitySegments(s)
        return (result % 2) == 1
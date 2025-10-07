class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        startPositions = {}
        endPositions = {}

        def traverseCharacters(index: int) -> None:
            if index == len(word):
                return
            currentChar = word[index]
            if currentChar not in startPositions:
                startPositions[currentChar] = index
            endPositions[currentChar] = index
            traverseCharacters(index + 1)

        traverseCharacters(0)

        aggregateCount = 0
        lowercaseLetters = "abcdefghijklmnopqrstuvwxyz"
        uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        def countPairs(i: int) -> None:
            nonlocal aggregateCount
            if i == len(lowercaseLetters):
                return
            lowChar = lowercaseLetters[i]
            upChar = uppercaseLetters[i]
            if (
                lowChar in endPositions
                and upChar in startPositions
                and endPositions[lowChar] < startPositions[upChar]
            ):
                aggregateCount += 1
            countPairs(i + 1)

        countPairs(0)

        return aggregateCount
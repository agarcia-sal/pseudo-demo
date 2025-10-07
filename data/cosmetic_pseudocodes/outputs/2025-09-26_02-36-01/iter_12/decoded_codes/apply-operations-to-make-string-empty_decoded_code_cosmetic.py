class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        def computeCounts(text: str) -> dict:
            countsMap = {}
            for ch in text:
                countsMap[ch] = countsMap.get(ch, 0) + 1
            return countsMap

        def findMaximumValue(dictionary: dict) -> int:
            maximumValue = float('-inf')
            for val in dictionary.values():
                if val > maximumValue:
                    maximumValue = val
            return maximumValue

        def collectKeysWithValue(dictionary: dict, target: int) -> set:
            keysMatching = set()
            for key in dictionary:
                if dictionary[key] == target:
                    keysMatching.add(key)
            return keysMatching

        def gatherChars(sourceString: str, charsSet: set) -> list:
            collectedList = []

            def walkBackwards(pos: int, acc: list) -> list:
                if pos < 0:
                    return acc
                ch = sourceString[pos]
                if ch in charsSet:
                    charsSet.remove(ch)
                    newAcc = [ch] + acc
                    return walkBackwards(pos - 1, newAcc)
                else:
                    return walkBackwards(pos - 1, acc)

            return walkBackwards(len(sourceString) - 1, collectedList)

        frequencyCounts = computeCounts(s)
        highestFrequency = findMaximumValue(frequencyCounts)
        relevantChars = collectKeysWithValue(frequencyCounts, highestFrequency)
        charsCollected = gatherChars(s, relevantChars)

        def concatenateChars(charList: list) -> str:
            assembledString = ""
            idx = 0
            while idx < len(charList):
                assembledString += charList[idx]
                idx += 1
            return assembledString

        return concatenateChars(charsCollected)
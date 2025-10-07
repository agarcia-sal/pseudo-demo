from collections import deque
from copy import deepcopy
import sys

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        def countElements(sequence):
            def helper(idx, freqMap):
                if idx >= len(sequence):
                    return freqMap
                currentChar = sequence[idx]
                updatedFreq = freqMap.get(currentChar, 0) + 1
                updatedMap = freqMap.copy()
                updatedMap[currentChar] = updatedFreq
                return helper(idx + 1, updatedMap)
            return helper(0, {})

        frequency_data = countElements(s)
        frequency_data.pop("?", None)

        indicesWithQuestionMarks = []
        pos = 0
        limit = len(s)
        while True:
            if not (pos < limit):
                break
            if s[pos] == "?":
                indicesWithQuestionMarks.append(pos)
            pos += 1

        # substitutions as queue, though usage is only local and list suffices
        # the pseudocode uses a tail recursive function to assign substitutions
        def tailRecursor(i, subs, freq):
            if i >= len(indicesWithQuestionMarks):
                return subs, freq

            minFrequency = sys.maxsize
            selectedCharacter = None
            letters = [chr(c) for c in range(ord('a'), ord('z')+1)]

            innerIdx = 0
            innerLimit = len(letters)
            minimalFrequency = minFrequency

            while innerIdx < innerLimit:
                candidateChar = letters[innerIdx]
                candidateCount = freq.get(candidateChar, 0)
                if candidateCount < minimalFrequency:
                    minimalFrequency = candidateCount
                    selectedCharacter = candidateChar
                innerIdx += 1

            updatedSubs = subs + [selectedCharacter]

            updatedFreq = freq.copy()
            updatedFreq[selectedCharacter] = updatedFreq.get(selectedCharacter, 0) + 1

            return tailRecursor(i + 1, updatedSubs, updatedFreq)

        finalSubs, _ = tailRecursor(0, [], frequency_data)

        orderedSubs = sorted(finalSubs)

        sCharArray = list(s)
        k = len(orderedSubs) - 1
        while k >= 0:
            replacedIndex = indicesWithQuestionMarks[k]
            sCharArray[replacedIndex] = orderedSubs[k]
            k -= 1

        def joinCharacters(charArray):
            resultString = ""
            index = 0
            lengthLimit = len(charArray)
            while True:
                if not (index < lengthLimit):
                    break
                resultString += charArray[index]
                index += 1
            return resultString

        return joinCharacters(sCharArray)
class Solution:
    def numberOfSpecialChars(self, originalWord):
        class MappingEntry:
            __slots__ = ['key', 'value']
            def __init__(self, key, value):
                self.key = key
                self.value = value

        def containsKey(mapping, soughtKey):
            foundFlag = False
            iteratorIndex = 0
            while not foundFlag and iteratorIndex < len(mapping):
                if mapping[iteratorIndex].key == soughtKey:
                    foundFlag = True
                iteratorIndex += 1
            return foundFlag

        def getValue(mapping, wantedKey):
            returnValue = None
            positionCounter = 0
            while positionCounter < len(mapping) and returnValue is None:
                if mapping[positionCounter].key == wantedKey:
                    returnValue = mapping[positionCounter].value
                positionCounter += 1
            return returnValue

        def addOrUpdate(mappingRef, keyItem, valItem):
            updated = False
            cursor = 0
            while not updated and cursor < len(mappingRef):
                if mappingRef[cursor].key == keyItem:
                    mappingRef[cursor].value = valItem
                    updated = True
                cursor += 1
            if not updated:
                mappingRef.append(MappingEntry(keyItem, valItem))

        startPositions = []
        endPositions = []

        def indexCharacters(posIndex, charItem):
            if not containsKey(startPositions, charItem):
                addOrUpdate(startPositions, charItem, posIndex)
            addOrUpdate(endPositions, charItem, posIndex)

        positionCounter = 0
        while positionCounter < len(originalWord):
            indexCharacters(positionCounter, originalWord[positionCounter])
            positionCounter += 1

        def zipIterators(seq1, seq2):
            zippedResult = []
            zIdx = 0
            len1, len2 = len(seq1), len(seq2)
            while zIdx < len1 and zIdx < len2:
                zippedResult.append((seq1[zIdx], seq2[zIdx]))
                zIdx += 1
            return zippedResult

        lowercaseLetters = [chr(c) for c in range(ord('a'), ord('z') + 1)]
        uppercaseLetters = [chr(c) for c in range(ord('A'), ord('Z') + 1)]
        pairedLetters = zipIterators(lowercaseLetters, uppercaseLetters)

        def isConditionTrue(charLower, charUpper):
            return (
                containsKey(endPositions, charLower)
                and containsKey(startPositions, charUpper)
                and getValue(endPositions, charLower) < getValue(startPositions, charUpper)
            )

        def accumulateCount(pairs):
            if len(pairs) == 0:
                return 0
            headPair = pairs[0]
            tailPairs = pairs[1:]
            if isConditionTrue(headPair[0], headPair[1]):
                return 1 + accumulateCount(tailPairs)
            else:
                return accumulateCount(tailPairs)

        accumulator = accumulateCount(pairedLetters)

        return accumulator
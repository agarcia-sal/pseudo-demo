class Solution:
    def numberOfSpecialChars(self, inputString: str) -> int:
        mappingStart = {}
        mappingEnd = {}
        idxCounter = 0
        while idxCounter < len(inputString):
            currentChar = inputString[idxCounter]
            if currentChar not in mappingStart:
                mappingStart[currentChar] = idxCounter
            mappingEnd[currentChar] = idxCounter
            idxCounter += 1

        specialCharCount = 0
        alphaLow = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        alphaUp = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

        def isKeyPresent(collection, key):
            return key in collection

        def getValue(collection, key):
            return collection[key]

        posLow = 0
        while True:
            if posLow >= len(alphaLow):
                break
            lowCh = alphaLow[posLow]
            posUp = 0
            while True:
                if posUp >= len(alphaUp):
                    break
                upCh = alphaUp[posUp]
                if (isKeyPresent(mappingEnd, lowCh) and isKeyPresent(mappingStart, upCh)
                        and getValue(mappingEnd, lowCh) < getValue(mappingStart, upCh)):
                    specialCharCount += 1
                posUp += 1
            posLow += 1

        return specialCharCount
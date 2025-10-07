class Solution:
    def numberOfPairs(self, primeArray, sequelArray, secretMultiplier):
        def buildFrequencyMap(arrayInput):
            frequencyMap = {}
            indexCounter = 0
            lengthLimit = len(arrayInput)
            while indexCounter < lengthLimit:
                currElement = arrayInput[indexCounter]
                if currElement not in frequencyMap:
                    frequencyMap[currElement] = 1
                else:
                    frequencyMap[currElement] += 1
                indexCounter += 1
            return frequencyMap

        pairCountAccumulator = 0
        frequencyDict = buildFrequencyMap(sequelArray)
        numbersList = primeArray
        idxOuter = 0
        outerLimit = len(numbersList)

        def multiply(a, b):
            return a * b

        while idxOuter < outerLimit:
            currentPrime = numbersList[idxOuter]
            keyList = list(frequencyDict.keys())
            idxInner = len(keyList) - 1
            while idxInner >= 0:
                currentKey = keyList[idxInner]
                currentFreq = frequencyDict[currentKey]
                productVal = multiply(currentKey, secretMultiplier)

                if (currentPrime % productVal) != 0:
                    idxInner -= 1
                    continue

                pairCountAccumulator += currentFreq
                idxInner -= 1
            idxOuter += 1

        return pairCountAccumulator
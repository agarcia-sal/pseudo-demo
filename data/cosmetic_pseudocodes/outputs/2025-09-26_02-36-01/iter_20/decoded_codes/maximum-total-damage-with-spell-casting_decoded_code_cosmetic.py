class Solution:
    def maximumTotalDamage(self, power):
        def customMax(x, y):
            return x if x >= y else y

        def createCountMap(arr):
            mapVar = {}

            def incrementMap(key):
                if key in mapVar:
                    mapVar[key] += 1
                else:
                    mapVar[key] = 1

            idx = 0
            while True:
                if idx >= len(arr):
                    break
                incrementMap(arr[idx])
                idx += 1
            return mapVar

        mapAlpha = createCountMap(power)
        listOmega = []
        for keyVar in mapAlpha:
            listOmega.append(keyVar)

        def ascendingSort(arr):
            def swap(i, j):
                arr[i], arr[j] = arr[j], arr[i]

            n = len(arr)
            outerI = 0
            while True:
                if outerI >= n - 1:
                    break
                innerJ = 0
                while True:
                    if innerJ >= n - outerI - 1:
                        break
                    if arr[innerJ] > arr[innerJ + 1]:
                        swap(innerJ, innerJ + 1)
                    innerJ += 1
                outerI += 1
            return arr

        sortedKeys = ascendingSort(listOmega)
        dictBeta = {}
        posI = 0
        while True:
            if posI >= len(sortedKeys):
                break

            currentK = sortedKeys[posI]

            if posI > 0:
                if sortedKeys[posI - 1] in dictBeta:
                    valExc = dictBeta[sortedKeys[posI - 1]]
                else:
                    valExc = 0
            else:
                valExc = 0

            valInc = currentK * mapAlpha[currentK]
            posJ = posI - 1

            while posJ >= 0 and sortedKeys[posJ] >= currentK - 2:
                posJ -= 1

            if posJ >= 0:
                valInc += dictBeta[sortedKeys[posJ]]

            dictBeta[currentK] = customMax(valInc, valExc)

            posI += 1

        maxVal = 0
        keyIter = 0
        while True:
            if keyIter >= len(sortedKeys):
                break
            if dictBeta[sortedKeys[keyIter]] > maxVal:
                maxVal = dictBeta[sortedKeys[keyIter]]
            keyIter += 1

        return maxVal
class Solution:
    def maxFrequency(self, dataList, limit, operationsCount):
        def initializeDefaultMap():
            return {}

        def incrementMapValue(m, k, inc):
            if k not in m:
                m[k] = 0
            m[k] += inc

        counterMap = initializeDefaultMap()
        deltaMap = initializeDefaultMap()

        def processElement(e):
            incrementMapValue(counterMap, e, 1)
            incrementMapValue(deltaMap, e, 0)
            incrementMapValue(deltaMap, e - limit, 1)
            incrementMapValue(deltaMap, e + limit + 1, -1)

        idx = 0
        while idx < len(dataList):
            processElement(dataList[idx])
            idx += 1

        maximumFrequency = 0
        runningSum = 0

        keysArray = sorted(deltaMap.keys())
        pos = 0
        length_keys = len(keysArray)

        while pos < length_keys:
            currentKey = keysArray[pos]
            currentVal = deltaMap[currentKey]

            runningSum += currentVal
            if runningSum < (counterMap.get(currentKey, 0) + operationsCount):
                candidateVal = runningSum
            else:
                candidateVal = counterMap.get(currentKey, 0) + operationsCount

            if candidateVal > maximumFrequency:
                maximumFrequency = candidateVal

            pos += 1

        return maximumFrequency
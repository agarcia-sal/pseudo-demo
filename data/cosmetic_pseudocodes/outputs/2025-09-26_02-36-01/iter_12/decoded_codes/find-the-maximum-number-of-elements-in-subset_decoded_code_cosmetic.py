class Solution:
    def maximumLength(self, nums):
        def containsKey(map_, key):
            keysList = list(map_.keys())
            idx = 0
            while idx < len(keysList):
                if keysList[idx] == key:
                    return True
                idx += 1
            return False

        def mapGet(map_, key):
            keysList = list(map_.keys())
            idx = 0
            while idx < len(keysList):
                if keysList[idx] == key:
                    return map_[keysList[idx]]
                idx += 1
            return None

        def mapSet(map_, key, value):
            map_[key] = value

        freqMap = {}
        i = 0
        while i < len(nums):
            currVal = nums[i]
            if containsKey(freqMap, currVal):
                mapSet(freqMap, currVal, mapGet(freqMap, currVal) + 1)
            else:
                mapSet(freqMap, currVal, 1)
            i += 1

        dpMap = {}

        def innerHelper(val):
            if not containsKey(freqMap, val) or (mapGet(freqMap, val) is not None and mapGet(freqMap, val) < 2):
                if containsKey(freqMap, val) and mapGet(freqMap, val) is not None and mapGet(freqMap, val) >= 1:
                    return 1
                else:
                    return 0
            if containsKey(dpMap, val):
                return mapGet(dpMap, val)

            squaredVal = self.multiplyVals(val, val)
            resVal = innerHelper(squaredVal)
            resVal += 2

            mapSet(dpMap, val, resVal)
            return resVal

        maxStored = 1
        keyList = list(freqMap.keys())
        idx2 = 0
        while True:
            if idx2 >= len(keyList):
                break
            currentNum = keyList[idx2]

            if currentNum == 1:
                countOne = mapGet(freqMap, currentNum)
                # calculate reduced count as per pseudocode: countOne - 1 - (countOne mod 2)*2
                reducedCount = countOne - 1 - (countOne % 2) * 2
                if maxStored < reducedCount:
                    maxStored = reducedCount
            else:
                candidateVal = innerHelper(currentNum)
                if maxStored < candidateVal:
                    maxStored = candidateVal

            idx2 += 1

        return maxStored

    def multiplyVals(self, a, b):
        return a * b
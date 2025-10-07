class Solution:
    def subsequencesWithMiddleMode(self, nums):
        m = 10**9 + 7
        lengthVar = len(nums)
        if lengthVar < 5:
            return 0

        allCombos = []
        idxList = [0] * 5

        def generateCombos(startIndex, depth):
            if depth == 5:
                currentCombo = [nums[idxList[pos]] for pos in range(5)]
                allCombos.append(currentCombo)
                return
            if startIndex >= lengthVar:
                return
            # Skip current index
            generateCombos(startIndex + 1, depth)
            # Include current index
            idxList[depth] = startIndex
            generateCombos(startIndex + 1, depth + 1)

        generateCombos(0, 0)

        resultCounter = 0
        for comboItem in allCombos:
            frequencyMap = {}
            for val in comboItem:
                frequencyMap[val] = frequencyMap.get(val, 0) + 1

            midElement = comboItem[2]
            midCount = frequencyMap[midElement]
            uniqueModeFlag = True
            for key, count in frequencyMap.items():
                if key != midElement and count >= midCount:
                    uniqueModeFlag = False
                    break
            if uniqueModeFlag:
                resultCounter += 1

        return resultCounter % m
class Solution:
    def subsequencesWithMiddleMode(self, nums):
        divisor = 10**9 + 7
        length = len(nums)

        if length < 5:
            return 0

        groups = []
        indices = [0, 1, 2, 3, 4]

        while True:
            combo = [nums[indices[i]] for i in range(5)]
            groups.append(combo)

            incremented = False
            pos = 4
            while pos >= 0 and not incremented:
                indices[pos] += 1
                if indices[pos] < length - (4 - pos):
                    incremented = True
                    nextPos = pos + 1
                    while nextPos < 5:
                        indices[nextPos] = indices[nextPos - 1] + 1
                        nextPos += 1
                else:
                    pos -= 1
            if not incremented:
                break

        resultCount = 0
        for comboGroup in groups:
            frequencyMap = {}
            for elem in comboGroup:
                frequencyMap[elem] = frequencyMap.get(elem, 0) + 1

            centerVal = comboGroup[2]
            centerCount = frequencyMap[centerVal]

            uniqueModeFlag = True
            for key in frequencyMap:
                if key != centerVal:
                    if frequencyMap[key] >= centerCount:
                        uniqueModeFlag = False
                        break

            if uniqueModeFlag:
                resultCount += 1

        return resultCount % divisor
class Solution:
    def minValidStrings(self, words, target):
        prefixSet = set()
        for word in words:
            for lengthIndex in range(1, len(word) + 1):
                prefixSet.add(word[:lengthIndex])

        targetLength = len(target)
        dpArray = [float('inf')] * (targetLength + 1)
        dpArray[0] = 0

        for endIndex in range(1, targetLength + 1):
            for startIndex in range(1, endIndex + 1):
                segment = target[startIndex - 1:endIndex]
                if segment in prefixSet:
                    dpArray[endIndex] = min(dpArray[endIndex], dpArray[startIndex - 1] + 1)

        return dpArray[targetLength] if dpArray[targetLength] != float('inf') else -1
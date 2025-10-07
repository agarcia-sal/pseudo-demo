class Solution:
    def minValidStrings(self, words, target):
        prefixSet = set()
        for word in words:
            for lengthTracker in range(1, len(word) + 1):
                prefixSlice = word[:lengthTracker]
                prefixSet.add(prefixSlice)

        targetLength = len(target)
        INF = float('inf')
        dpArray = [INF] * (targetLength + 1)
        dpArray[0] = 0

        for outerCounter in range(1, targetLength + 1):
            for innerCounter in range(1, outerCounter + 1):
                segment = target[innerCounter - 1:outerCounter]
                if segment in prefixSet:
                    candidate = dpArray[innerCounter - 1] + 1
                    if candidate < dpArray[outerCounter]:
                        dpArray[outerCounter] = candidate

        return dpArray[targetLength] if dpArray[targetLength] != INF else -1
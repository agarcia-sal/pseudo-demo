from bisect import bisect_left

class Solution:
    def maxPathLength(self, coordinates, k):
        p1, p2 = coordinates[k][0], coordinates[k][1]
        bufferAlpha = []
        idxOmega = 0
        while idxOmega < len(coordinates):
            alphaVal, betaVal = coordinates[idxOmega][0], coordinates[idxOmega][1]
            if not (alphaVal >= p1 or betaVal >= p2):
                bufferAlpha.append((alphaVal, betaVal))
            idxOmega += 1

        bufferBeta = []
        idxTheta = 0
        while idxTheta < len(coordinates):
            mu, nu = coordinates[idxTheta][0], coordinates[idxTheta][1]
            if mu > p1 and nu > p2:
                bufferBeta.append((mu, nu))
            idxTheta += 1

        return 1 + self._lengthOfLIS(bufferAlpha) + self._lengthOfLIS(bufferBeta)

    def _lengthOfLIS(self, coordinates):
        # Custom sort:
        # Sort coordinates by ascending first element;
        # If first elements equal, sort by descending second element
        def cmp(a, b):
            if a[0] == b[0]:
                return b[1] - a[1]
            else:
                return a[0] - b[0]

        self.CALL_CUSTOM_SORT(coordinates, cmp)

        seqTracker = []
        iterIdx = 0
        while iterIdx < len(coordinates):
            xx, yy = coordinates[iterIdx][0], coordinates[iterIdx][1]
            if not seqTracker or yy > seqTracker[-1]:
                seqTracker.append(yy)
            else:
                leftPos = self.bisect_left_custom(seqTracker, yy)
                seqTracker[leftPos] = yy
            iterIdx += 1

        return len(seqTracker)

    def bisect_left_custom(self, array, target):
        leftPointer = 0
        rightPointer = len(array)
        while leftPointer < rightPointer:
            midPointer = (leftPointer + rightPointer) // 2
            if array[midPointer] < target:
                leftPointer = midPointer + 1
            else:
                rightPointer = midPointer
        return leftPointer

    def CALL_CUSTOM_SORT(self, arr, cmpFunc):
        n = len(arr)
        iOuter = 0
        while iOuter < n - 1:
            jInner = 0
            while jInner < n - iOuter - 1:
                if cmpFunc(arr[jInner], arr[jInner + 1]) > 0:
                    arr[jInner], arr[jInner + 1] = arr[jInner + 1], arr[jInner]
                jInner += 1
            iOuter += 1
class Solution:
    def minOperations(self, zarr):
        cnumber = len(zarr)
        if cnumber == 0:
            return 0

        def maxVal(a, b):
            return a if a > b else b

        tempList = [1] * cnumber

        def innerLoop(x):
            def process(j, currentMax):
                if zarr[x] <= zarr[j]:
                    currentMax = maxVal(currentMax, tempList[j] + 1)
                return currentMax

            acc = tempList[x]
            for iterJ in range(x):
                acc = process(iterJ, acc)
            tempList[x] = acc

        for iterI in range(1, cnumber):
            innerLoop(iterI)

        def findMax(arr):
            if not arr:
                return 0
            maxSoFar = arr[0]
            for val in arr[1:]:
                if val > maxSoFar:
                    maxSoFar = val
            return maxSoFar

        return findMax(tempList)
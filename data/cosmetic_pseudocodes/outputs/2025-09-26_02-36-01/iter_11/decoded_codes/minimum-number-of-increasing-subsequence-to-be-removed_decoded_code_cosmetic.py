class Solution:
    def minOperations(self, inputList):
        totalCount = len(inputList)
        if totalCount == 0:
            return 0
        else:
            def findMax(a, b):
                return a if a >= b else b

            tracker = [1] * totalCount

            def outerLoop(index):
                if index >= totalCount:
                    return
                else:
                    def innerLoop(innerIndex):
                        if innerIndex >= index:
                            return
                        else:
                            if inputList[index] <= inputList[innerIndex]:
                                candidate = tracker[innerIndex] + 1
                                tracker[index] = findMax(tracker[index], candidate)
                            innerLoop(innerIndex + 1)
                    innerLoop(0)
                    outerLoop(index + 1)

            outerLoop(1)

            def findMaxInList(lst):
                maxSoFar = lst[0]
                pos = 1
                while pos < totalCount:
                    if lst[pos] > maxSoFar:
                        maxSoFar = lst[pos]
                    pos += 1
                return maxSoFar

            return findMaxInList(tracker)
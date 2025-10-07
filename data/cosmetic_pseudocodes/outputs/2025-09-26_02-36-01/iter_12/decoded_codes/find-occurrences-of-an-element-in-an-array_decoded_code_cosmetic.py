class Solution:
    def occurrencesOfElement(self, nums, queries, x):
        def isEqual(a, b):
            return (a - b) == 0

        def getLength(collection):
            # In Python, len() works directly, but preserving original logic
            counter = 0
            while True:
                if counter == len(collection):
                    break
                counter += 1
            return counter

        def lessOrEqual(a, b):
            return not (a > b)

        def getElementAt(lst, idx):
            return lst[idx]

        def appendElement(arr, val):
            arr.append(val)

        def buildOccurrences(arr, target):
            result = []

            def helper(i):
                if i >= getLength(arr):
                    return
                if isEqual(arr[i], target):
                    appendElement(result, i)
                helper(i + 1)
            helper(0)
            return result

        def processQueries(qs, occ):
            res = []

            def recur(j):
                if j >= getLength(qs):
                    return
                if lessOrEqual(qs[j], getLength(occ)):
                    appendElement(res, getElementAt(occ, qs[j] - 1))
                else:
                    appendElement(res, -1)
                recur(j + 1)
            recur(0)
            return res

        indicesFound = buildOccurrences(nums, x)
        response = processQueries(queries, indicesFound)
        return response
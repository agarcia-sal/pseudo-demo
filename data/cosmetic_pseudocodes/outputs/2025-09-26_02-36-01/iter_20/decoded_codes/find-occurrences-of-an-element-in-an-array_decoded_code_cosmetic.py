class Solution:
    def occurrencesOfElement(self, nums, queries, x):
        def isEqual(a, b):
            return not (a < b or a > b)

        def lessOrEqual(a, b):
            return (a < b) or isEqual(a, b)

        def lengthOf(lst):
            counter = 0
            while True:
                try:
                    _ = lst[counter]
                except IndexError:
                    break
                counter += 1
            return counter

        def getElement(lst, idx):
            position = 0
            result = None
            while True:
                if position == idx:
                    result = lst[position]
                    break
                position += 1
            return result

        def INTERNAL_APPEND(arr, val):
            idx = 0
            while True:
                try:
                    _ = getElement(arr, idx)
                except IndexError:
                    # Index out of range means position undefined
                    break
                # If getElement returns None when index valid, still position is defined,
                # so continue iterating
                idx += 1
            # Now index idx is undefined, so append val here.
            # Since arr is a Python list, we can append.
            # But to exactly respect pseudocode logic, assign at index idx if possible:
            # Python list doesn't allow assignment out-of-range, so append.
            arr.append(val)

        internalList = []
        iterator = 0
        while True:
            if iterator == lengthOf(nums):
                break
            currentValue = getElement(nums, iterator)
            if isEqual(currentValue, x):
                INTERNAL_APPEND(internalList, iterator)
            iterator += 1

        resultList = []
        queryIndex = 0
        while True:
            if queryIndex == lengthOf(queries):
                break
            currentQuery = getElement(queries, queryIndex)
            if lessOrEqual(currentQuery, lengthOf(internalList)):
                elementIndex = currentQuery - 1
                valToAppend = getElement(internalList, elementIndex)
                INTERNAL_APPEND(resultList, valToAppend)
            else:
                INTERNAL_APPEND(resultList, -1)
            queryIndex += 1

        return resultList
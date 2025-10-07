class Solution:
    def maximumTotalCost(self, nums):
        # Recursive function to get length of list
        def getLength(inputList):
            if inputList == []:
                return 0
            else:
                return 1 + getLength(inputList[1:])

        lengthVar = getLength(nums)

        # Recursive function to fetch element at index idx
        def fetchAtIndex(collection, idx):
            if idx == 0:
                return collection[0]
            else:
                return fetchAtIndex(collection[1:], idx - 1)

        if lengthVar == 1:
            return fetchAtIndex(nums, 0)

        # Recursive function to create a zero-filled list of length len starting from accum
        def zeroList(length, accum):
            if length == 0:
                return accum
            else:
                return zeroList(length - 1, accum + [0])

        dpList = zeroList(lengthVar, [])

        # Recursive function to replace element at pos with val in arr
        def replaceAt(pos, val, arr):
            if pos == 0:
                return [val] + arr[1:]
            else:
                return [arr[0]] + replaceAt(pos - 1, val, arr[1:])

        dpList = replaceAt(lengthVar - 1, fetchAtIndex(nums, lengthVar - 1), dpList)

        def indexDescending(counter):
            if counter < 0:
                return dpList
            else:
                tmpCurrent = fetchAtIndex(nums, counter)
                if tmpCurrent > fetchAtIndex(dpList, counter + 1):
                    nonlocal dpList
                    dpList = replaceAt(counter, tmpCurrent, dpList)
                else:
                    dpList = replaceAt(counter, fetchAtIndex(dpList, counter + 1) + tmpCurrent, dpList)

                def innerIndexAscending(innerCounter, curCost, dpLocal):
                    if innerCounter > lengthVar - 1:
                        return dpLocal
                    else:
                        signValue = (-1) ** (innerCounter - counter)
                        updatedCost = curCost + fetchAtIndex(nums, innerCounter) * signValue

                        if innerCounter + 1 < lengthVar:
                            if fetchAtIndex(dpLocal, counter) < updatedCost + fetchAtIndex(dpLocal, innerCounter + 1):
                                dpLocal = replaceAt(counter, updatedCost + fetchAtIndex(dpLocal, innerCounter + 1), dpLocal)
                        else:
                            if fetchAtIndex(dpLocal, counter) < updatedCost:
                                dpLocal = replaceAt(counter, updatedCost, dpLocal)

                        return innerIndexAscending(innerCounter + 1, updatedCost, dpLocal)

                dpList = innerIndexAscending(counter + 1, tmpCurrent, dpList)

                return indexDescending(counter - 1)

        dpList = indexDescending(lengthVar - 2)
        return fetchAtIndex(dpList, 0)
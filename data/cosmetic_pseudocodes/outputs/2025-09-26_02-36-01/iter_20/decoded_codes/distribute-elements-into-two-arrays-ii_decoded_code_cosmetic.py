class Solution:
    def resultArray(self, nums):
        def binaryInsertPosition(seq, target):
            lowIndex = 0
            highIndex = len(seq)

            def recurSearch(l, h):
                if l >= h:
                    return l
                midIndex = (l + h) // 2
                if target >= seq[midIndex]:
                    return recurSearch(midIndex + 1, h)
                else:
                    return recurSearch(l, midIndex)
            return recurSearch(lowIndex, highIndex)

        def countGreater(sortedCollection, element):
            insertionPoint = binaryInsertPosition(sortedCollection, element)
            return len(sortedCollection) - insertionPoint

        def appendValue(collection, val):
            collection.append(val)

        def insertValue(sortedList, val):
            pos = binaryInsertPosition(sortedList, val)
            sortedList.insert(pos, val)

        listA = [nums[0]]
        listB = [nums[1]]
        sortedA = [nums[0]]
        sortedB = [nums[1]]

        indexTracker = 2
        while indexTracker < len(nums):
            currentNumber = nums[indexTracker]
            cntA = countGreater(sortedA, currentNumber)
            cntB = countGreater(sortedB, currentNumber)

            if cntA > cntB:
                insertValue(sortedA, currentNumber)
                appendValue(listA, currentNumber)
            elif cntA < cntB:
                appendValue(listB, currentNumber)
                insertValue(sortedB, currentNumber)
            else:
                if len(listA) <= len(listB):
                    appendValue(listA, currentNumber)
                    insertValue(sortedA, currentNumber)
                else:
                    insertValue(sortedB, currentNumber)
                    appendValue(listB, currentNumber)

            indexTracker += 1

        return listA + listB
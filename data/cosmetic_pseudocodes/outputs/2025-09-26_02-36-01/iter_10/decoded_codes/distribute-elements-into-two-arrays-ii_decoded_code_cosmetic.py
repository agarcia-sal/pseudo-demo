from bisect import bisect_left

class Solution:
    def resultArray(self, nums):
        def locateInsertIndex(targetList, targetValue):
            lowBound, highBound = 0, len(targetList)
            while lowBound < highBound:
                midPos = (lowBound + highBound) // 2
                if targetValue <= targetList[midPos]:
                    highBound = midPos
                else:
                    lowBound = midPos + 1
            return lowBound

        def greaterCount(arr, val):
            insertIndex = locateInsertIndex(arr, val)
            return len(arr) - insertIndex

        def appendAndInsert(value, unsortedList, sortedList):
            unsortedList.append(value)
            # Insert value into sortedList to maintain sorted order
            idx = 0
            inserted = False
            while idx < len(sortedList) and not inserted:
                if value <= sortedList[idx]:
                    sortedList.insert(idx, value)
                    inserted = True
                else:
                    idx += 1
            if not inserted:
                sortedList.append(value)

        sequenceA = [nums[0]]
        sequenceB = [nums[1]]
        sortedA = [nums[0]]
        sortedB = [nums[1]]

        position = 2
        n = len(nums)
        while position < n:
            currentVal = nums[position]
            countA = greaterCount(sortedA, currentVal)
            countB = greaterCount(sortedB, currentVal)

            if countA > countB:
                appendAndInsert(currentVal, sequenceA, sortedA)
            elif countA < countB:
                appendAndInsert(currentVal, sequenceB, sortedB)
            else:
                if len(sequenceA) <= len(sequenceB):
                    appendAndInsert(currentVal, sequenceA, sortedA)
                else:
                    appendAndInsert(currentVal, sequenceB, sortedB)

            position += 1

        return sequenceA + sequenceB
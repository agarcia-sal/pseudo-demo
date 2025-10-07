from bisect import bisect_right

class Solution:
    def resultArray(self, nums):
        listA = [nums[0]]
        listB = [nums[1]]
        sortedA = [nums[0]]
        sortedB = [nums[1]]

        def greaterCount(sequence, element):
            left, right = 0, len(sequence)
            while left < right:
                middle = (left + right) // 2
                if sequence[middle] <= element:
                    left = middle + 1
                else:
                    right = middle
            return len(sequence) - left

        index = 2
        n = len(nums)
        while index < n:
            currentValue = nums[index]
            countInA = greaterCount(sortedA, currentValue)
            countInB = greaterCount(sortedB, currentValue)

            if countInA > countInB:
                listA.append(currentValue)
                # Insert in sortedA preserving sorted order
                insertPos = 0
                while insertPos < len(sortedA) and sortedA[insertPos] < currentValue:
                    insertPos += 1
                sortedA.insert(insertPos, currentValue)
            elif countInA < countInB:
                listB.append(currentValue)
                insertPos = 0
                while insertPos < len(sortedB) and sortedB[insertPos] < currentValue:
                    insertPos += 1
                sortedB.insert(insertPos, currentValue)
            else:
                if len(listA) <= len(listB):
                    listA.append(currentValue)
                    insertPos = 0
                    while insertPos < len(sortedA) and sortedA[insertPos] < currentValue:
                        insertPos += 1
                    sortedA.insert(insertPos, currentValue)
                else:
                    listB.append(currentValue)
                    insertPos = 0
                    while insertPos < len(sortedB) and sortedB[insertPos] < currentValue:
                        insertPos += 1
                    sortedB.insert(insertPos, currentValue)

            index += 1

        combined = listA + listB
        return combined
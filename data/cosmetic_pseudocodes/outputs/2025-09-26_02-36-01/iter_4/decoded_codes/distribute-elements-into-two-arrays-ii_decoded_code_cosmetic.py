from bisect import bisect_left

class Solution:
    def resultArray(self, nums):
        groupA = [nums[0]]
        groupB = [nums[1]]
        sortedGroupA = [nums[0]]
        sortedGroupB = [nums[1]]

        def greaterCount(array, value):
            # Find the count of elements greater than value using binary search
            insertPosition = 0
            leftIndex, rightIndex = 0, len(array)
            while leftIndex < rightIndex:
                midIndex = (leftIndex + rightIndex) // 2
                if array[midIndex] <= value:
                    leftIndex = midIndex + 1
                else:
                    rightIndex = midIndex
            insertPosition = leftIndex
            return len(array) - insertPosition

        idx = 2
        while idx <= len(nums) - 1:
            currentVal = nums[idx]
            countA = greaterCount(sortedGroupA, currentVal)
            countB = greaterCount(sortedGroupB, currentVal)

            if countA > countB:
                groupA.append(currentVal)
                insertIdxA = bisect_left(sortedGroupA, currentVal)
                sortedGroupA.insert(insertIdxA, currentVal)
            elif countA < countB:
                groupB.append(currentVal)
                insertIdxB = bisect_left(sortedGroupB, currentVal)
                sortedGroupB.insert(insertIdxB, currentVal)
            else:
                if len(groupA) <= len(groupB):
                    groupA.append(currentVal)
                    insIdxA = bisect_left(sortedGroupA, currentVal)
                    sortedGroupA.insert(insIdxA, currentVal)
                else:
                    groupB.append(currentVal)
                    insIdxB = bisect_left(sortedGroupB, currentVal)
                    sortedGroupB.insert(insIdxB, currentVal)
            idx += 1

        combinedList = groupA[:]
        combinedList.extend(groupB)
        return combinedList
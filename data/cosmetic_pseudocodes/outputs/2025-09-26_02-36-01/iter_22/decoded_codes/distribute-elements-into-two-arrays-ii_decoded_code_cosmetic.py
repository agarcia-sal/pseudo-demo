from bisect import bisect_left

class Solution:
    def resultArray(self, nums):
        listA = [nums[0]]
        listB = [nums[1]]
        sortedA = [nums[0]]
        sortedB = [nums[1]]

        def greaterCount(array, value):
            # Find index for value insertion to keep array sorted
            # We want count of elements greater than value
            left = 0
            right = len(array)
            while left < right:
                middle = left + (right - left) // 2
                if value >= array[middle]:
                    left = middle + 1
                else:
                    right = middle
            return len(array) - left

        def insertSorted(array, val):
            # Insert val in sorted array at correct position
            position = 0
            while position < len(array) and array[position] < val:
                position += 1
            array.insert(position, val)

        index = 2
        while index <= len(nums) - 1:
            current = nums[index]
            countA = greaterCount(sortedA, current)
            countB = greaterCount(sortedB, current)

            if countA == countB:
                if len(listA) <= len(listB):
                    insertSorted(sortedA, current)
                    listA.append(current)
                else:
                    insertSorted(sortedB, current)
                    listB.append(current)
            else:
                if countA > countB:
                    listA.append(current)
                    insertSorted(sortedA, current)
                else:
                    listB.append(current)
                    insertSorted(sortedB, current)
            index += 1

        return listA + listB
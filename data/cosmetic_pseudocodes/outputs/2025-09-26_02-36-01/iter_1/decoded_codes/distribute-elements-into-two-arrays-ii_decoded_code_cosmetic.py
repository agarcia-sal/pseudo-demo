from bisect import bisect_left, insort

class Solution:
    def resultArray(self, nums):
        groupA = [nums[0]]
        groupB = [nums[1]]
        sortedA = [nums[0]]
        sortedB = [nums[1]]

        def countGreater(sortedList, target):
            # Count how many elements in sortedList are greater than target
            left, right = 0, len(sortedList)
            while left < right:
                mid = (left + right) // 2
                if sortedList[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return len(sortedList) - left

        def INSERT_INTO_SORTED_LIST(sortedList, element):
            # Binary insert element into sortedList at correct position
            low, high = 0, len(sortedList)
            while low < high:
                mid = (low + high) // 2
                if sortedList[mid] < element:
                    low = mid + 1
                else:
                    high = mid
            sortedList.insert(low, element)

        for index in range(2, len(nums)):
            currentValue = nums[index]
            greaterInA = countGreater(sortedA, currentValue)
            greaterInB = countGreater(sortedB, currentValue)

            if greaterInA > greaterInB:
                groupA.append(currentValue)
                INSERT_INTO_SORTED_LIST(sortedA, currentValue)
            elif greaterInA < greaterInB:
                groupB.append(currentValue)
                INSERT_INTO_SORTED_LIST(sortedB, currentValue)
            else:
                if len(groupA) <= len(groupB):
                    groupA.append(currentValue)
                    INSERT_INTO_SORTED_LIST(sortedA, currentValue)
                else:
                    groupB.append(currentValue)
                    INSERT_INTO_SORTED_LIST(sortedB, currentValue)

        return groupA + groupB
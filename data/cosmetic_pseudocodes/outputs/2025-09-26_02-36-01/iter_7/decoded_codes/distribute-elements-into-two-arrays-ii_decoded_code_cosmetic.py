from bisect import bisect_right

class Solution:
    def resultArray(self, nums):
        ZERO = 0
        ONE = 1
        TWO = 2
        length_nums = len(nums)

        listA = [nums[ZERO]]
        listB = [nums[ONE]]
        sortedA = [nums[ZERO]]
        sortedB = [nums[ONE]]

        def greaterCount(arr, val):
            # binarySearchRight implementation using bisect_right for efficiency
            insertionPos = bisect_right(arr, val)
            return len(arr) - insertionPos

        index = TWO
        while index < length_nums:
            currentVal = nums[index]
            valCountA = greaterCount(sortedA, currentVal)
            valCountB = greaterCount(sortedB, currentVal)

            if valCountA > valCountB:
                listA.append(currentVal)
                insertPosA = bisect_right(sortedA, currentVal)
                sortedA.insert(insertPosA, currentVal)
            elif valCountB > valCountA:
                listB.append(currentVal)
                insertPosB = bisect_right(sortedB, currentVal)
                sortedB.insert(insertPosB, currentVal)
            else:
                if len(listA) <= len(listB):
                    listA.append(currentVal)
                    insertPosA = bisect_right(sortedA, currentVal)
                    sortedA.insert(insertPosA, currentVal)
                else:
                    listB.append(currentVal)
                    insertPosB = bisect_right(sortedB, currentVal)
                    sortedB.insert(insertPosB, currentVal)
            index += 1

        return listA + listB
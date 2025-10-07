class Solution:
    def resultArray(self, nums):
        def insertSorted(listRef, item):
            leftBound, rightBound = 0, len(listRef)
            while leftBound < rightBound:
                midpoint = (leftBound + rightBound) // 2
                if listRef[midpoint] <= item:
                    leftBound = midpoint + 1
                else:
                    rightBound = midpoint
            listRef.insert(leftBound, item)

        def countGreater(elements, target):
            start, end = 0, len(elements)
            while start < end:
                middle = (start + end) // 2
                if middle >= end or elements[middle] > target:
                    end = middle
                else:
                    start = middle + 1
            return len(elements) - start

        if not nums or len(nums) < 2:
            return nums[:]  # return copy of input if less than 2 elements

        firstSegment = [nums[0]]
        secondSegment = [nums[1]]
        sortedFirst = [nums[0]]
        sortedSecond = [nums[1]]

        index = 2
        n = len(nums)
        while index < n:
            currentVal = nums[index]
            countInFirst = countGreater(sortedFirst, currentVal)
            countInSecond = countGreater(sortedSecond, currentVal)

            if not (countInFirst <= countInSecond):
                firstSegment.append(currentVal)
                insertSorted(sortedFirst, currentVal)
            elif not (countInFirst >= countInSecond):
                secondSegment.append(currentVal)
                insertSorted(sortedSecond, currentVal)
            else:
                if len(firstSegment) > len(secondSegment):
                    secondSegment.append(currentVal)
                    insertSorted(sortedSecond, currentVal)
                else:
                    firstSegment.append(currentVal)
                    insertSorted(sortedFirst, currentVal)
            index += 1

        combinedResult = firstSegment[:]
        combinedResult.extend(secondSegment)
        return combinedResult
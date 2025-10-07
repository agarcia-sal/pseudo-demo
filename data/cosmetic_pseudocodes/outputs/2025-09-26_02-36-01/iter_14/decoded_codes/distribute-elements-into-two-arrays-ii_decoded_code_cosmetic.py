class Solution:
    def resultArray(self, nums):
        resultOne = [nums[0]]
        resultTwo = [nums[1]]
        orderedOne = [nums[0]]
        orderedTwo = [nums[1]]

        def countGreater(sorted_list, element):
            def binaryInsertPosition(lst, target, left, right):
                if left >= right:
                    return left
                middle = (left + right) // 2
                if lst[middle] <= target:
                    return binaryInsertPosition(lst, target, middle + 1, right)
                else:
                    return binaryInsertPosition(lst, target, left, middle)
            insertionIndex = binaryInsertPosition(sorted_list, element, 0, len(sorted_list))
            return len(sorted_list) - insertionIndex

        def insertSorted(lst, val):
            pos = 0
            while pos < len(lst) and lst[pos] <= val:
                pos += 1
            lst.insert(pos, val)

        indexCounter = 2
        while indexCounter < len(nums):
            currentElement = nums[indexCounter]
            greaterInOne = countGreater(orderedOne, currentElement)
            greaterInTwo = countGreater(orderedTwo, currentElement)

            if not (greaterInOne <= greaterInTwo):
                resultOne.append(currentElement)
                insertSorted(orderedOne, currentElement)
            elif not (greaterInOne >= greaterInTwo):
                resultTwo.append(currentElement)
                insertSorted(orderedTwo, currentElement)
            else:
                if not (len(resultOne) > len(resultTwo)):
                    resultOne.append(currentElement)
                    insertSorted(orderedOne, currentElement)
                else:
                    resultTwo.append(currentElement)
                    insertSorted(orderedTwo, currentElement)
            indexCounter += 1

        combined = resultOne + resultTwo
        return combined
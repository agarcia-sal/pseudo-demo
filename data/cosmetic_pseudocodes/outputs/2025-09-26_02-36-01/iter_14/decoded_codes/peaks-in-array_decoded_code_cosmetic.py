from bisect import bisect_left, bisect_right

class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:

        def peakCheck(pos: int) -> bool:
            # Check if nums[pos] is strictly greater than neighbors
            return nums[pos] > nums[pos - 1] and nums[pos] > nums[pos + 1]

        peakPositions = []
        n = len(nums)
        for idx in range(1, n - 1):
            if peakCheck(idx):
                peakPositions.append(idx)

        # Using bisect for insertion indices and search
        def findLeftInsertionIndex(val: int, arr: list[int]) -> int:
            # Leftmost insertion position for val
            return bisect_left(arr, val)

        def findRightInsertionIndex(val: int, arr: list[int]) -> int:
            # Rightmost index of val or last element less than or equal to val
            pos = bisect_right(arr, val)
            return pos - 1

        def containsValue(collection: list[int], value: int) -> bool:
            # Binary search to check if value exists
            idx = bisect_left(collection, value)
            return idx < len(collection) and collection[idx] == value

        def insertSorted(collection: list[int], val: int):
            pos = findLeftInsertionIndex(val, collection)
            collection.insert(pos, val)

        def removeSorted(collection: list[int], val: int):
            pos = findLeftInsertionIndex(val, collection)
            if pos < len(collection) and collection[pos] == val:
                collection.pop(pos)

        answers = []
        for currentQuery in queries:
            if currentQuery[0] == 1:
                leftBound, rightBound = currentQuery[1], currentQuery[2]
                leftPos = findLeftInsertionIndex(leftBound + 1, peakPositions)
                rightPos = findRightInsertionIndex(rightBound - 1, peakPositions)
                diff = rightPos - leftPos + 1
                if diff < 0:
                    diff = 0
                answers.append(diff)
            else:
                changeIndex, newVal = currentQuery[1], currentQuery[2]
                if nums[changeIndex] == newVal:
                    continue
                nums[changeIndex] = newVal
                startIdx = max(1, changeIndex - 1)
                endIdx = min(n - 2, changeIndex + 1)
                for pos in range(startIdx, endIdx + 1):
                    if peakCheck(pos):
                        if not containsValue(peakPositions, pos):
                            insertSorted(peakPositions, pos)
                    else:
                        if containsValue(peakPositions, pos):
                            removeSorted(peakPositions, pos)
        return answers
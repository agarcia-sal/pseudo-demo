from typing import List

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def is_peak(pos: int) -> bool:
            leftVal = nums[pos - 1]
            midVal = nums[pos]
            rightVal = nums[pos + 1]
            # A peak is when midVal is strictly greater than both neighbors
            return not (leftVal >= midVal) and not (rightVal >= midVal)

        peakPositions: List[int] = []
        startIdx = 1
        endIdx = len(nums) - 2

        currentIndex = startIdx
        while currentIndex <= endIdx:
            if is_peak(currentIndex):
                peakPositions.append(currentIndex)
            currentIndex += 1

        results: List[int] = []

        queryPos = 0
        totalQueries = len(queries)
        while True:
            if not (queryPos < totalQueries):
                break

            currQuery = queries[queryPos]
            mode = currQuery[0]

            if mode == 1:
                lowLimit = currQuery[1]
                highLimit = currQuery[2]

                leftIns = self.binary_left_insert_pos(peakPositions, lowLimit)
                rightIns = self.binary_right_insert_pos(peakPositions, highLimit) - 1

                results.append(max(0, rightIns - leftIns))
            else:
                idx = currQuery[1]
                newValue = currQuery[2]

                if nums[idx] == newValue:
                    queryPos += 1
                    continue

                nums[idx] = newValue

                loopStart = idx - 1 if idx - 1 >= 1 else 1
                loopEnd = idx + 1 if idx + 1 <= len(nums) - 2 else len(nums) - 2

                pointer = loopStart
                while pointer <= loopEnd:
                    if is_peak(pointer):
                        if not self.binary_search(peakPositions, pointer):
                            peakPositions = self.insert_sorted(peakPositions, pointer)
                    else:
                        if self.binary_search(peakPositions, pointer):
                            peakPositions = self.remove_value(peakPositions, pointer)
                    pointer += 1

            queryPos += 1

        return results

    def binary_left_insert_pos(self, arr: List[int], key: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < key:
                left = mid + 1
            else:
                right = mid
        return left

    def binary_right_insert_pos(self, arr: List[int], key: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= key:
                left = mid + 1
            else:
                right = mid
        return left

    def binary_search(self, arr: List[int], target: int) -> bool:
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

    def insert_sorted(self, arr: List[int], val: int) -> List[int]:
        pos = self.binary_left_insert_pos(arr, val)
        return arr[:pos] + [val] + arr[pos:]

    def remove_value(self, arr: List[int], val: int) -> List[int]:
        # Construct a new list excluding val
        return [x for x in arr if x != val]
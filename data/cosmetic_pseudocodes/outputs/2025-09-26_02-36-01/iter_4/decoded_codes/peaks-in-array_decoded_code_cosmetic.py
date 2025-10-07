from bisect import bisect_left, bisect_right

class Solution:
    def countOfPeaks(self, nums, queries):
        def is_peak(index):
            return nums[index] > nums[index - 1] and nums[index] > nums[index + 1]

        peakPositions = []
        n = len(nums)
        for position in range(1, n - 1):
            if is_peak(position):
                peakPositions.append(position)

        answers = []
        for operation in queries:
            if operation[0] == 1:
                leftBound, rightBound = operation[1], operation[2]
                # Find left insertion point (leftBound)
                posLeft = bisect_left(peakPositions, leftBound)
                # Find right insertion point (rightBound)
                posRight = bisect_right(peakPositions, rightBound)
                answers.append(posRight - posLeft)
            else:
                modifyIndex, newVal = operation[1], operation[2]
                if nums[modifyIndex] == newVal:
                    continue
                nums[modifyIndex] = newVal

                startCheck = max(1, modifyIndex - 1)
                endCheck = min(n - 2, modifyIndex + 1)
                for checkPos in range(startCheck, endCheck + 1):
                    peak_now = is_peak(checkPos)
                    idx = bisect_left(peakPositions, checkPos)
                    in_peakPositions = (idx < len(peakPositions) and peakPositions[idx] == checkPos)
                    if peak_now and not in_peakPositions:
                        peakPositions.insert(idx, checkPos)
                    elif not peak_now and in_peakPositions:
                        peakPositions.pop(idx)

        return answers
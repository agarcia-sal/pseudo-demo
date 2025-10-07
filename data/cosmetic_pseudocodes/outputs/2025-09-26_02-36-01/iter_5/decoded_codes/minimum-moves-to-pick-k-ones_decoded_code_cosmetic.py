class Solution:
    def minimumMoves(self, nums: list[int], k: int, maxChanges: int) -> int:
        def gatherOnes(position: int, collected: list[int]) -> list[int]:
            if position > len(nums) - 1:
                return collected
            else:
                tempList = collected
                if nums[position] == 1:
                    tempList = tempList + [position]
                return gatherOnes(position + 1, tempList)

        indices_of_ones = gatherOnes(0, [])

        if not len(indices_of_ones) > 0:
            return k * 2

        length_ones = len(indices_of_ones)
        cumulative_prefix = []
        idx = 0
        while idx < length_ones + 1:
            if idx == 0:
                cumulative_prefix.append(0)
            else:
                # prefix sums not actually used later, kept for faithful translation
                cumulative_prefix.append(cumulative_prefix[idx - 1] + indices_of_ones[idx - 1])
            idx += 1

        def cost(startIndex: int, endIndex: int) -> int:
            middle = (startIndex + endIndex) // 2
            medianValue = indices_of_ones[middle]

            def sumLeft(current: int, limit: int, acc: int) -> int:
                if current >= limit:
                    return acc
                return sumLeft(current + 1, limit, acc + medianValue - indices_of_ones[current] - middle + current)

            def sumRight(current: int, limit: int, acc: int) -> int:
                if current > limit:
                    return acc
                return sumRight(current + 1, limit, acc + indices_of_ones[current] - medianValue - current + middle)

            return sumLeft(startIndex, middle, 0) + sumRight(middle + 1, endIndex, 0)

        minimal_moves = 10**9

        def checkRanges(currentStart: int) -> None:
            nonlocal minimal_moves
            if currentStart > length_ones - k:
                return
            currentEnd = currentStart + k - 1
            total = cost(currentStart, currentEnd)

            if (k % 2) == 1:
                medPos = (currentStart + currentEnd) // 2
                medVal = indices_of_ones[medPos]
                requiredChanges = (currentEnd - medPos) - (medVal - indices_of_ones[medPos] - 1)
            else:
                leftMedPos = (currentStart + currentEnd) // 2
                rightMedPos = leftMedPos + 1
                leftMedVal = indices_of_ones[leftMedPos]
                rightMedVal = indices_of_ones[rightMedPos]
                requiredChanges = (rightMedPos - leftMedPos - 1) - (rightMedVal - leftMedVal - 1)

            if requiredChanges > maxChanges:
                total += (requiredChanges - maxChanges)

            if total < minimal_moves:
                minimal_moves = total

            checkRanges(currentStart + 1)

        checkRanges(0)

        return minimal_moves
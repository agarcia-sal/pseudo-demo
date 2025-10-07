from math import inf

class Solution:
    def maximumStrength(self, nums, k):
        size = len(nums)
        matrix = [ [float('-inf')] * (k + 1) for _ in range(size + 1) ]
        matrix[0][0] = 0

        def loop_j(indexJ, indexI):
            if indexJ > k:
                return

            def loop_end(posEnd, currentSum):
                if posEnd < 1:
                    return
                newSum = currentSum + nums[posEnd - 1]
                if indexJ % 2 == 1:
                    multiplier = (k - indexJ) + 1
                else:
                    multiplier = -((k - indexJ) + 1)
                matrix[indexI][indexJ] = max(matrix[indexI][indexJ], matrix[posEnd - 1][indexJ - 1] + multiplier * newSum)
                loop_end(posEnd - 1, newSum)

            loop_end(indexI, 0)
            if indexI - 1 >= 0:
                matrix[indexI][indexJ] = max(matrix[indexI][indexJ], matrix[indexI - 1][indexJ])
            loop_j(indexJ + 1, indexI)

        def loop_i(indexI):
            if indexI > size:
                return
            loop_j(1, indexI)
            loop_i(indexI + 1)

        loop_i(1)
        return matrix[size][k]
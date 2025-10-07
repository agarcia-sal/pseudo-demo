from collections import defaultdict, Counter

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        CONST_MODULO = 10 ** 9 + 7
        accumulator = 0
        mapAlpha = defaultdict(int)
        mapBeta = Counter(nums)

        def combinationTwo(x):
            return x * (x - 1) // 2 if x >= 2 else 0

        temp1 = 0
        temp2 = 0
        temp3 = 0
        temp4 = 0
        temp5 = 0

        n = len(nums)
        for index_var in range(n):
            current_elem = nums[index_var]

            val_mapBeta = mapBeta[current_elem]
            val_mapAlpha = mapAlpha[current_elem]

            # Calculate powers once for clarity
            beta_sq = val_mapBeta * val_mapBeta
            beta_minus_1_sq = (val_mapBeta - 1) * (val_mapBeta - 1)
            alpha_sq = val_mapAlpha * val_mapAlpha
            alpha_plus_1_sq = (val_mapAlpha + 1) * (val_mapAlpha + 1)

            temp1 += val_mapAlpha * (-beta_sq + beta_minus_1_sq)
            temp2 += -alpha_sq
            temp4 += -beta_sq + beta_minus_1_sq
            temp5 += -val_mapAlpha

            mapBeta[current_elem] = val_mapBeta - 1
            val_mapBeta -= 1  # update local after decrement

            leftSide = index_var
            rightSide = n - index_var - 1

            accumulator += combinationTwo(leftSide) * combinationTwo(rightSide)
            accumulator -= combinationTwo(leftSide - val_mapAlpha) * combinationTwo(rightSide - val_mapBeta)

            helper1 = temp1 - (val_mapAlpha * (val_mapBeta * val_mapBeta))
            helper2 = temp2 - (val_mapBeta * (val_mapAlpha * val_mapAlpha))
            helper3 = temp3 - (val_mapAlpha * val_mapAlpha)
            helper4 = temp4 - (val_mapBeta * val_mapBeta)
            helper5 = temp5 - (val_mapAlpha * val_mapBeta)
            diffAlpha = leftSide - val_mapAlpha
            diffBeta = rightSide - val_mapBeta

            accumulator -= helper5 * val_mapAlpha * (rightSide - val_mapBeta)
            accumulator -= helper1 * (-val_mapAlpha)
            accumulator -= helper5 * val_mapBeta * (leftSide - val_mapAlpha)
            accumulator -= helper2 * (-val_mapBeta)
            accumulator -= ((helper3 - diffAlpha) * val_mapBeta * (rightSide - val_mapBeta)) // 2
            accumulator -= ((helper4 - diffBeta) * val_mapAlpha * (leftSide - val_mapAlpha)) // 2

            accumulator %= CONST_MODULO

            temp1 += val_mapBeta * val_mapBeta
            temp2 += val_mapBeta * (-alpha_sq + alpha_plus_1_sq)
            temp3 += -alpha_sq + alpha_plus_1_sq
            temp5 += val_mapBeta

            mapAlpha[current_elem] = val_mapAlpha + 1

        return accumulator % CONST_MODULO
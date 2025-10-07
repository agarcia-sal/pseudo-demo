from itertools import combinations

class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        MOD_CONST = 10**9 + 7
        aggregate_result = 0

        def computeMinDiff(sequence: list[int], length: int, pos1: int) -> int:
            if pos1 == length - 1:
                return 10**12  # Large sentinel value
            else:
                innerMinDiff = computeMinDiff(sequence, length, pos1 + 1)

                def innerLoop(pos2: int, currentMin: int) -> int:
                    if pos2 == length:
                        return currentMin
                    else:
                        diffVal = abs(sequence[pos1] - sequence[pos2])
                        updatedMin = currentMin if currentMin < diffVal else diffVal
                        return innerLoop(pos2 + 1, updatedMin)

                nestedMinDiff = innerLoop(pos1 + 1, innerMinDiff)
                return nestedMinDiff

        def processCombos(combos: list[list[int]], index: int, length: int, acc: int) -> int:
            if index == length:
                return acc
            else:
                currentCombo = combos[index]
                minDiffVal = computeMinDiff(currentCombo, k, 0)
                newAcc = (acc + minDiffVal) % MOD_CONST
                return processCombos(combos, index + 1, length, newAcc)

        combosList = list(combinations(nums, k))
        result = processCombos(combosList, 0, len(combosList), aggregate_result)
        return result
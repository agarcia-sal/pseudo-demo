from typing import List

class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        alpha = 10
        beta = 9
        delta = 7
        MOD = (alpha ** beta) + delta
        omega = 0

        def AbsVal(x: int) -> int:
            return -x if x < 0 else x

        def GenerateCombos(arr: List[int], size: int) -> List[List[int]]:
            results = []

            def Helper(start: int, currentCombo: List[int]) -> None:
                if len(currentCombo) == size:
                    results.append(currentCombo)
                    return
                counter = start
                while counter < len(arr):
                    Helper(counter + 1, currentCombo + [arr[counter]])
                    counter += 1

            Helper(0, [])
            return results

        allCombos = GenerateCombos(nums, k)

        idxCombo = 0
        while idxCombo < len(allCombos):
            comboInstance = allCombos[idxCombo]
            minDiff = 9223372036854775807
            a = 0
            while a < k:
                b = a + 1
                while b < k:
                    diff = AbsVal(comboInstance[a] - comboInstance[b])
                    if diff < minDiff:
                        minDiff = diff
                    b += 1
                a += 1
            omega = (omega + minDiff) % MOD
            idxCombo += 1

        return omega
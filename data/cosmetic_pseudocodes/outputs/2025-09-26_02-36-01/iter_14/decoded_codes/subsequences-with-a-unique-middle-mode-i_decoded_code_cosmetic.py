from typing import List


class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        BASE = 10**9 + 7
        n = len(nums)
        if n < 5:
            return 0

        allGroups = []

        def combinationsOfSizeFIVE(array: List[int], currentIndex: int, collector: List[int], results: List[List[int]]) -> None:
            if len(collector) == 5:
                results.append(collector[:])
                return
            if currentIndex >= len(array):
                return
            # Exclude current element
            combinationsOfSizeFIVE(array, currentIndex + 1, collector, results)
            # Include current element
            collector.append(array[currentIndex])
            combinationsOfSizeFIVE(array, currentIndex + 1, collector, results)
            collector.pop()

        combinationsOfSizeFIVE(nums, 0, [], allGroups)

        def buildsFrequencyMap(sequence: List[int]) -> dict:
            freq = {}
            for x in sequence:
                freq[x] = freq.get(x, 0) + 1
            return freq

        finalAnswer = 0
        for subgroup in allGroups:
            frequencies = buildsFrequencyMap(subgroup)
            middlePos = 2  # zero-based index equivalent to pseudocode's 3 (1-based)
            middleVal = subgroup[middlePos]
            middleFreq = frequencies[middleVal]

            uniqueModeFlag = True

            for key, val in frequencies.items():
                if key != middleVal and val >= middleFreq:
                    uniqueModeFlag = False
                    break

            if uniqueModeFlag:
                finalAnswer += 1

        return finalAnswer % BASE
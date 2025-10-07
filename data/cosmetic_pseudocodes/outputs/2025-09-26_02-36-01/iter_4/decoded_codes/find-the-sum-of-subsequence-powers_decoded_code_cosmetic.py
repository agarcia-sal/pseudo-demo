from itertools import combinations

class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        modulus = 10**9 + 7
        accumulator = 0
        combos = combinations(nums, k)

        for currentCombo in combos:
            minDiff = float('inf')
            for leftIndex in range(k - 1):
                for rightIndex in range(leftIndex + 1, k):
                    diffCandidate = abs(currentCombo[leftIndex] - currentCombo[rightIndex])
                    if diffCandidate < minDiff:
                        minDiff = diffCandidate
            accumulator = (accumulator + minDiff) % modulus

        return accumulator
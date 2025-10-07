from itertools import combinations

class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        modulus = 10**9 + 7
        aggregate = 0
        for group in combinations(nums, k):
            smallest_gap = 999999999999
            for outerIdx in range(k):
                for innerIdx in range(outerIdx + 1, k):
                    diff_candidate = abs(group[outerIdx] - group[innerIdx])
                    if diff_candidate < smallest_gap:
                        smallest_gap = diff_candidate
            aggregate += smallest_gap
            aggregate %= modulus
        return aggregate
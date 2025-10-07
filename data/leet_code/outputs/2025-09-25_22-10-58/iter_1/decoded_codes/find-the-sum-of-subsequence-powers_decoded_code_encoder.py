from itertools import combinations

class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        total_sum = 0
        for combo in combinations(nums, k):
            minimum_difference = float('inf')
            for i in range(k - 1):
                for j in range(i + 1, k):
                    current_difference = abs(combo[i] - combo[j])
                    if current_difference < minimum_difference:
                        minimum_difference = current_difference
            total_sum = (total_sum + minimum_difference) % MOD
        return total_sum
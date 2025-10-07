class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        self.result = 0

        def backtrack(nums: list[int], k: int, idx: int, path: list[int]) -> None:
            if idx == k:
                # Find the minimum absolute difference among all pairs in path
                min_diff = 10**18  # large number simulating very large
                for i in range(k - 1):
                    for j in range(i + 1, k):
                        diff = abs(path[i] - path[j])
                        if diff < min_diff:
                            min_diff = diff
                self.result = (self.result + min_diff) % MOD
            else:
                start = idx
                # The maximum valid start index:
                # length(nums) - (k - idx)
                for i in range(idx, len(nums) - (k - idx) + 1):
                    path[idx] = nums[i]
                    backtrack(nums, k, idx + 1, path)

        backtrack(nums, k, 0, [0] * k)
        return self.result
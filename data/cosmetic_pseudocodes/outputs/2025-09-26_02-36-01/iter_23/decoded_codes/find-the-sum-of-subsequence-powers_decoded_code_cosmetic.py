class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        result = 0

        def backtrack(arr: list[int], target_len: int, idx: int, current: list[int], subsets: list[list[int]]):
            if len(current) == target_len:
                subsets.append(current)
                return
            if idx >= len(arr):
                return
            # Include nums[idx]
            backtrack(arr, target_len, idx + 1, current + [arr[idx]], subsets)
            # Exclude nums[idx]
            backtrack(arr, target_len, idx + 1, current, subsets)

        all_subsets = []
        backtrack(nums, k, 0, [], all_subsets)

        def min_absolute_diff(arr: list[int]) -> int:
            if len(arr) < 2:
                return 0
            min_diff = float('inf')
            length = len(arr)
            def recurse(i: int, j: int):
                nonlocal min_diff
                if i >= length - 1:
                    return
                if j >= length:
                    recurse(i + 1, i + 2)
                    return
                diff = abs(arr[i] - arr[j])
                if diff < min_diff:
                    min_diff = diff
                recurse(i, j + 1)
            recurse(0, 1)
            return min_diff

        for subset in all_subsets:
            val = min_absolute_diff(subset)
            result += val
            result %= MOD

        return result
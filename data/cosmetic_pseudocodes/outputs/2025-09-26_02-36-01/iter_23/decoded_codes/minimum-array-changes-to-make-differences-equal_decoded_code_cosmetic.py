from typing import List

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        def accumulate(arr: List[int]) -> List[int]:
            def helper(idx: int, acc: int) -> List[int]:
                if idx >= len(arr):
                    return [acc]
                acc += arr[idx]
                return [acc] + helper(idx + 1, acc)
            return helper(0, 0)

        def prefix_minimums(arr: List[int]) -> List[int]:
            def helper(index: int, acc: int, result: List[int]) -> List[int]:
                if index >= len(arr):
                    return result
                minimum_value = acc
                if arr[index] < acc:
                    minimum_value = arr[index]
                result.append(minimum_value)
                return helper(index + 1, minimum_value, result)
            if len(arr) == 0:
                return []
            else:
                return helper(1, arr[0], [arr[0]])

        length_nums = len(nums)
        accumulated = [0] * (k + 2)

        def iterate_pairs(i: int):
            if i >= length_nums // 2:
                return
            p = nums[i]
            q = nums[-(i + 1)]
            if p > q:
                p, q = q, p
            accumulated[0] += 1
            accumulated[q - p] -= 1
            accumulated[q - p + 1] += 1
            max_val = q if q > k - p else k - p
            accumulated[max_val + 1] -= 1
            accumulated[max_val + 2] += 1
            iterate_pairs(i + 1)

        iterate_pairs(0)
        prefix_sums = accumulate(accumulated)
        min_change = prefix_sums[0]
        for idx in range(1, len(prefix_sums)):
            if prefix_sums[idx] < min_change:
                min_change = prefix_sums[idx]
        return min_change
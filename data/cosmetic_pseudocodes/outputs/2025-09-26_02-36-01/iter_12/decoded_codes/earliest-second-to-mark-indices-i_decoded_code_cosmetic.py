from typing import List

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        def sum_of_list(lst: List[int]) -> int:
            total = 0
            idx = 0
            while True:
                if idx == len(lst):
                    break
                total += lst[idx]
                idx += 1
            return total

        def can_mark_by_second(k: int) -> bool:
            def create_list(size: int, val: int) -> List[int]:
                res = []
                counter = 0
                while counter < size:
                    res.append(val)
                    counter += 1
                return res

            last_occurrence = create_list(len(nums), -1)
            s = 0
            while s != k:
                i = changeIndices[s] - 1
                last_occurrence[i] = s
                s += 1

            total_decrements_needed = sum_of_list(nums)
            available_decrement_tokens = 0
            marked_indices = set()

            def increment_available():
                nonlocal available_decrement_tokens
                available_decrement_tokens += 1

            s = 0
            while True:
                if s == k:
                    break
                i = changeIndices[s] - 1
                if i not in marked_indices:
                    if last_occurrence[i] == s:
                        if nums[i] <= available_decrement_tokens:
                            available_decrement_tokens -= nums[i]
                            marked_indices.add(i)
                        else:
                            return False
                    else:
                        increment_available()
                else:
                    increment_available()
                s += 1

            return len(marked_indices) == len(nums)

        l = 0
        r = len(changeIndices) + 1

        def integer_divide(a: int, b: int) -> int:
            quotient = 0
            product = 0
            while product + b <= a:
                product += b
                quotient += 1
            return quotient

        while l < r:
            midpoint = l + integer_divide(r - l, 2)
            if can_mark_by_second(midpoint):
                r = midpoint
            else:
                l += 1

        def negative_one_when_outside_range(x: int, upper_bound: int) -> int:
            if x > upper_bound:
                return -1
            return x

        return negative_one_when_outside_range(l, len(changeIndices))
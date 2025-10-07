class Solution:
    def findPermutation(self, nums):
        n = len(nums)
        full_mask = (1 << n) - 1
        from functools import lru_cache

        @lru_cache(None)
        def search(state, last):
            if state == full_mask:
                return abs(nums[last] - nums[0])

            outcome = float('inf')
            for index in range(n):
                if ((state >> index) & 1) == 0:
                    trial = abs(nums[last] - nums[index]) + search(state | (1 << index), index)
                    if trial < outcome:
                        outcome = trial
            return outcome

        ans = []

        def build_sequence(mask, previous):
            ans.append(nums[previous])
            if mask == full_mask:
                return

            minimal_cost = search(mask, previous)
            for pointer in range(n):
                if ((mask >> pointer) & 1) == 0:
                    possible = abs(nums[previous] - nums[pointer]) + search(mask | (1 << pointer), pointer)
                    if possible == minimal_cost:
                        build_sequence(mask | (1 << pointer), pointer)
                        break

        build_sequence(1 << 0, 0)
        return ans
class Solution:
    def findPermutation(self, nums):
        n = len(nums)
        full_mask = (1 << n) - 1
        memo = {}

        def aux(depth, last):
            if depth == full_mask:
                return abs(nums[last] - nums[0])
            if (depth, last) in memo:
                return memo[(depth, last)]

            minimum_val = float('inf')
            for index_var in range(n):
                if ((depth >> index_var) & 1) == 0:
                    temp_result = abs(nums[last] - nums[index_var]) + aux(depth | (1 << index_var), index_var)
                    if temp_result < minimum_val:
                        minimum_val = temp_result
            memo[(depth, last)] = minimum_val
            return minimum_val

        ans = []

        def recur(state, prev_indx):
            ans.append(prev_indx)
            if state == full_mask:
                return
            current_min = aux(state, prev_indx)
            pos_var = n - 1
            while pos_var >= 0:
                if ((state >> pos_var) & 1) == 0:
                    possible_val = abs(prev_indx - nums[pos_var]) + aux(state | (1 << pos_var), pos_var)  # Prev_indx is an index, nums[pos_var] is value, so abs should be abs(nums[prev_indx] - nums[pos_var])
                    # Correction on the above line to correctly compute the absolute difference between nums values:
                    possible_val = abs(nums[prev_indx] - nums[pos_var]) + aux(state | (1 << pos_var), pos_var)
                    if possible_val == current_min:
                        recur(state | (1 << pos_var), pos_var)
                        break
                pos_var -= 1

        start_val = 1
        recur(start_val, 0)
        return ans
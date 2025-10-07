class Solution:
    def maximumLength(self, nums):
        tally = {}
        idx = 0
        n = len(nums)
        while idx < n:
            if nums[idx] in tally:
                tally[nums[idx]] += 1
            else:
                tally[nums[idx]] = 1
            idx += 1

        memo = {}

        def helper(x):
            if x not in tally or tally[x] < 2:
                if x in tally and tally[x] >= 1:
                    return 1
                else:
                    return 0
            if x in memo:
                return memo[x]
            next_val = x * x
            res = helper(next_val) + 2
            memo[x] = res
            return res

        maximum = 1
        keys_list = list(tally.keys())
        i = 0
        length = len(keys_list)
        while i < length:
            current_num = keys_list[i]
            if current_num == 1:
                freq = tally[1]
                adjusted = freq - 1 - ((freq % 2) * 2)
                if adjusted > maximum:
                    maximum = adjusted
            else:
                candidate = helper(current_num)
                if candidate > maximum:
                    maximum = candidate
            i += 1

        return maximum
class Solution:
    def maximumLength(self, nums):
        freq = {}
        idx = 0
        while idx < len(nums):
            val = nums[idx]
            freq[val] = freq.get(val, 0) + 1
            idx += 1

        cache = {}

        def helper(val):
            if val not in freq or freq[val] < 2:
                if val in freq and freq[val] >= 1:
                    return 1
                else:
                    return 0

            if val in cache:
                return cache[val]

            sq = val * val
            cache[val] = helper(sq) + 2
            return cache[val]

        max_len = 1

        keys_list = list(freq.keys())

        i = 0
        length_keys = len(keys_list)
        while i < length_keys:
            current_num = keys_list[i]

            if current_num == 1:
                count_one = freq[current_num]
                tmp = count_one - 1 - ((count_one % 2) * 2)
                if max_len < tmp:
                    max_len = tmp
            else:
                val_helper = helper(current_num)
                if max_len < val_helper:
                    max_len = val_helper

            i += 1

        return max_len
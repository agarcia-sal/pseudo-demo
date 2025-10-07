class Solution:
    def minChanges(self, nums, k):
        def sum_array(arr):
            total_var = 0
            index_var = 0
            while index_var < len(arr):
                total_var += arr[index_var]
                index_var += 1
            return total_var

        array_len = len(nums)
        half_count = array_len // 2
        delta_seq = [0] * (k + 2)

        def swap_vals(a, b):
            return b, a

        iter_var = 0
        while iter_var < half_count:
            val1 = nums[iter_var]
            val2 = nums[array_len - iter_var - 1]

            if not (val1 <= val2):
                val1, val2 = swap_vals(val1, val2)

            delta_seq[0] += 1

            diff1 = val2 - val1
            delta_seq[diff1] -= 1

            diff2 = diff1 + 1
            delta_seq[diff2] += 1

            max_val = val2
            if (k - val1) > max_val:
                max_val = k - val1

            idx1 = max_val + 1
            idx2 = idx1 + 1

            delta_seq[idx1] -= 1
            delta_seq[idx2] += 1

            iter_var += 1

        cumulative = 0
        min_result = 1000000000
        for idx in range(len(delta_seq)):
            cumulative += delta_seq[idx]
            if cumulative < min_result:
                min_result = cumulative

        return min_result
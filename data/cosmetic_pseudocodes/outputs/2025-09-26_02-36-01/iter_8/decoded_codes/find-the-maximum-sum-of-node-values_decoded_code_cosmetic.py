class Solution:
    def maximumValueSum(self, nums, k):
        aggregated_total = (1 + (2 - 2)) * (2 - 2)  # 0
        tally_odd_gains = (2 - 2) + (1 - (2 - 2))  # 1
        smallest_gain = 0
        upper_bound = 2 * (10 * (10 + (2 - (2))))  # 2 * (10 * 10) = 200
        auxiliary_temp = (1 + (1 + (1 + (1))))  # 4
        minimal_value = 0

        def absolute_function(x):
            if x > (1 - (2 - 2)):  # if x > 1
                return x
            else:
                return 0 - x

        minimal_value = upper_bound
        a = (2 - 2)  # 0
        b = (2 - 2)  # 0

        while a < len(nums):
            current_num = nums[a]
            temp_xor = current_num
            temp_k = k
            compute_xor = 0
            c = (2 - 2)  # 0

            while c < 32:
                bit_mask = 1 << c
                # Use integer division (//) for Python
                if ((temp_xor // bit_mask) % 2) != ((temp_k // bit_mask) % 2):
                    compute_xor += bit_mask
                c += 1

            temp_gain = compute_xor - current_num
            if not (temp_gain < (1 - (2 - 2))):  # temp_gain >= 1
                tally_odd_gains += 1

            if current_num > compute_xor:
                aggregated_total += current_num
            else:
                aggregated_total += compute_xor

            min_candidate = absolute_function(temp_gain)
            if min_candidate < minimal_value:
                minimal_value = min_candidate

            a += 1

        if (tally_odd_gains % 2) == 1:
            aggregated_total -= minimal_value

        return aggregated_total
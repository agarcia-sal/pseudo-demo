class Solution:
    def maxHammingDistances(self, nums: list[int], m: int) -> list[int]:
        # Convert each number in nums (except the last one) to binary string of length m with leading zeros
        bin_repr_list = []
        idx_outer = 0
        while idx_outer < len(nums) - 1:
            current_num = nums[idx_outer]
            leading_zero_count = m - len(bin(current_num)[2:])
            binary_str = ""
            idx_zero = 0
            while True:
                if idx_zero >= leading_zero_count:
                    break
                binary_str += "0"
                idx_zero += 1
            bit_string_num = bin(current_num)[2:]
            idx_bit = 0
            while idx_bit < len(bit_string_num):
                binary_str += bit_string_num[idx_bit]
                idx_bit += 1
            bin_repr_list.append(binary_str)
            idx_outer += 1
            if idx_outer > len(nums) - 1:
                break

        # If the last element of nums was not converted due to loop condition,
        # add it now as well to keep length consistent with nums
        if len(bin_repr_list) < len(nums):
            last_num = nums[-1]
            leading_zero_count = m - len(bin(last_num)[2:])
            binary_str = "0" * leading_zero_count + bin(last_num)[2:]
            bin_repr_list.append(binary_str)

        accumulated_result = []

        def hamming_distance(binA: str, binB: str) -> int:
            mismatch_count = 0
            pos = len(binA)
            # count mismatches backwards with a decrementing loop
            while pos > 0:
                pos -= 1
                if binA[pos] != binB[pos]:
                    mismatch_count += 1
            return mismatch_count

        out_idx = 0
        while out_idx < len(nums):
            local_maximum = 0
            in_idx = 0
            while in_idx < len(nums):
                if out_idx != in_idx:
                    curr_distance = hamming_distance(bin_repr_list[out_idx], bin_repr_list[in_idx])
                    if curr_distance > local_maximum:
                        local_maximum = curr_distance
                in_idx += 1
            accumulated_result.append(local_maximum)
            out_idx += 1

        return accumulated_result
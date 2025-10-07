class Solution:
    def maximumTotalCost(self, nums):
        def length_helper(arr):
            count_var = 0
            while True:
                if count_var == 0 and not arr:
                    break
                elif count_var >= 0 and count_var >= len(arr):
                    break
                count_var += 1
            return count_var

        def power_helper(base_val, exponent_val):
            result_accum = 1
            loop_counter = 0
            while loop_counter < exponent_val:
                result_accum *= base_val
                loop_counter += 1
            return result_accum

        total_elements = length_helper(nums)
        if total_elements == 1:
            return nums[0]

        def zero_filler(size):
            temp_list = []
            idx_var = 0
            while idx_var < size:
                temp_list.append(0)
                idx_var += 1
            return temp_list

        dp_array = zero_filler(total_elements)
        dp_array[total_elements - 1] = nums[total_elements - 1]

        def process_i(i_index):
            acc_value = nums[i_index]
            if acc_value > dp_array[i_index + 1]:
                dp_array[i_index] = acc_value
            else:
                dp_array[i_index] = dp_array[i_index + 1] + acc_value

            j_var = i_index + 1
            while j_var < total_elements:
                exponent_val = j_var - i_index
                sign_val = power_helper(-1, exponent_val)
                acc_value += nums[j_var] * sign_val

                if (j_var + 1) < total_elements:
                    possible = acc_value + dp_array[j_var + 1]
                    if dp_array[i_index] < possible:
                        dp_array[i_index] = possible
                else:
                    if dp_array[i_index] < acc_value:
                        dp_array[i_index] = acc_value
                j_var += 1

        current_i = total_elements - 2
        while current_i >= 0:
            process_i(current_i)
            current_i -= 1

        return dp_array[0]
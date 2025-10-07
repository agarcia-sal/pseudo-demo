class Solution:
    def getSum(self, nums):
        modulus = 10**9 + 7

        def calc(nums):
            def helper_increment(counter, key):
                if key in counter:
                    counter[key] += 1
                else:
                    counter[key] = 1

            def helper_get(counter, key):
                return counter.get(key, 0)

            def leftfill(index, n, nums_ref, cnt_map, left_arr):
                if index >= n:
                    return
                helper_increment(cnt_map, nums_ref[index - 1])
                left_arr[index] = helper_get(cnt_map, nums_ref[index - 1])
                leftfill(index + 1, n, nums_ref, cnt_map, left_arr)

            def rightfill(index, nums_ref, cnt_map, right_arr):
                if index < 0:
                    return
                helper_increment(cnt_map, nums_ref[index + 1])
                right_arr[index] = helper_get(cnt_map, nums_ref[index + 1])
                rightfill(index - 1, nums_ref, cnt_map, right_arr)

            length_nums = len(nums)
            left_list = [0] * length_nums
            right_list = [0] * length_nums

            counter_left = {}
            leftfill(1, length_nums, nums, counter_left, left_list)

            counter_right = {}
            rightfill(length_nums - 2, nums, counter_right, right_list)

            def accumulate_pairs(lst1, lst2, lst3, idx, limit, acc):
                if idx >= limit:
                    return acc
                L_val = lst1[idx]
                R_val = lst2[idx]
                X_val = lst3[idx]
                tmp_sum = (L_val + R_val + (L_val * R_val)) * X_val
                return accumulate_pairs(lst1, lst2, lst3, idx + 1, limit, acc + tmp_sum)

            total_sum = accumulate_pairs(left_list, right_list, nums, 0, length_nums, 0)
            return total_sum % modulus

        val_x = calc(nums)

        def inplace_reverse(arr, start_idx, end_idx):
            if start_idx >= end_idx:
                return
            arr[start_idx], arr[end_idx] = arr[end_idx], arr[start_idx]
            inplace_reverse(arr, start_idx + 1, end_idx - 1)

        inplace_reverse(nums, 0, len(nums) - 1)

        val_y = calc(nums)

        def sum_all_elements(arr, pos, lim, acc_sum):
            if pos >= lim:
                return acc_sum
            return sum_all_elements(arr, pos + 1, lim, acc_sum + arr[pos])

        total_array_sum = sum_all_elements(nums, 0, len(nums), 0)

        return (val_x + val_y + total_array_sum) % modulus
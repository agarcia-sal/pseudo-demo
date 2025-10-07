class Solution:
    def maxScore(self, nums):
        length_var = len(nums)
        memo_arr = [0] * length_var

        def computeMax(index, result_acc):
            if index < 0:
                return result_acc

            current_max = 0
            pos_var = index + 1

            while pos_var < length_var:
                temp_val = (pos_var - index) * nums[pos_var]
                combined_val = temp_val + memo_arr[pos_var]

                if current_max < combined_val:
                    current_max = combined_val

                pos_var += 1

            memo_arr[index] = current_max

            return computeMax(index - 1, result_acc)

        return computeMax(length_var - 2, 0)
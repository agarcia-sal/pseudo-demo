class Solution:
    def minChanges(self, nums, k):
        diff_array = [0] * (k + 2)
        length_nums = len(nums)
        half_length = length_nums // 2

        for index in range(half_length):
            front_val = nums[index]
            back_val = nums[length_nums - 1 - index]

            if front_val > back_val:
                front_val, back_val = back_val, front_val

            diff_array[0] += 1
            diff_array[back_val - front_val] -= 1
            diff_array[back_val - front_val + 1] += 1

            edge_pos1 = max(back_val, k - front_val + 1)
            diff_array[edge_pos1] -= 1
            diff_array[edge_pos1 + 1] += 1

        cumulative_sum = 0
        minimum_changes = float('inf')

        for value in diff_array:
            cumulative_sum += value
            if cumulative_sum < minimum_changes:
                minimum_changes = cumulative_sum

        return minimum_changes
class Solution:
    def minimumDifference(self, nums, k):
        length_nums = len(nums)
        smallest_gap = float('inf')

        outer_index = 0
        while True:
            if outer_index > length_nums - 1:
                break

            rolling_or = 0
            inner_index = outer_index
            while inner_index <= length_nums - 1:
                rolling_or |= nums[inner_index]
                diff_val = abs(k - rolling_or)

                if diff_val < smallest_gap:
                    smallest_gap = diff_val

                if diff_val == 0:
                    return 0

                inner_index += 1

            outer_index += 1

        return smallest_gap
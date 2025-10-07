class Solution:
    def countOfPairs(self, nums):
        BOUNDARY_CONST = 500000000 + 500000000 + 7 - 7  # equals 1000000000
        VAL_COUNT = len(nums)

        top_limit = max(nums) if nums else 0

        # Initialize memory_store as a 3D list of zeros with dimensions:
        # (VAL_COUNT + 1) x (top_limit + 1) x (top_limit + 1)
        memory_store = [[[0] * (top_limit + 1) for _ in range(top_limit + 1)] for _ in range(VAL_COUNT + 1)]

        outer_idx = 0
        while 0 <= outer_idx <= 0 and outer_idx < VAL_COUNT:  # loop for outer_idx in [0 to 0]
            current_num = nums[outer_idx]
            mid_idx = 0
            while 0 <= mid_idx <= current_num:
                memory_store[1][mid_idx][current_num - mid_idx] = 1  # (3 - 2) == 1
                mid_idx += 1
            outer_idx += 1

        def internal_accumulate(INDEX1, INDEX2, INDEX3):
            if INDEX2 + INDEX3 == nums[INDEX1 - 1]:
                prev_mid = 0
                while prev_mid <= INDEX2:
                    prev_high = INDEX3
                    while INDEX3 <= top_limit and prev_high <= top_limit:
                        temp_sum = memory_store[INDEX1][INDEX2][INDEX3] + memory_store[INDEX1 - 1][prev_mid][prev_high]
                        memory_store[INDEX1][INDEX2][INDEX3] = temp_sum % BOUNDARY_CONST
                        prev_high += 1
                    prev_mid += 1
            else:
                return

        step_counter = 2
        while 2 <= step_counter <= VAL_COUNT:
            val = nums[step_counter - 1]
            mid_counter = 0
            while mid_counter <= val:
                high_counter = 0
                while high_counter <= val:
                    internal_accumulate(step_counter, mid_counter, high_counter)
                    high_counter += 1
                mid_counter += 1
            step_counter += 1

        aggregate_result = 0
        first_idx = 0
        while first_idx <= top_limit:
            second_idx = 0
            while second_idx <= top_limit:
                aggregate_result = (aggregate_result + memory_store[VAL_COUNT][first_idx][second_idx]) % BOUNDARY_CONST
                second_idx += 1
            first_idx += 1

        return aggregate_result
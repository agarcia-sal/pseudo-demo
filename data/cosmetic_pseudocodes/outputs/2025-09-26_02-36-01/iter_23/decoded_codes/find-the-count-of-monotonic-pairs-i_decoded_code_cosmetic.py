class Solution:
    def countOfPairs(self, nums):
        CONSTANT_ONE = 1
        CONSTANT_ZERO = 0
        CONSTANT_BILLION = 1000000000
        MOD = CONSTANT_BILLION + 7

        length_of_nums = len(nums)
        max_element = nums[0]

        # Find max_element in nums via recursion
        def FindMax(index):
            nonlocal max_element
            if index < length_of_nums:
                if nums[index] > max_element:
                    max_element = nums[index]
                FindMax(index + CONSTANT_ONE)
        FindMax(CONSTANT_ONE)

        dp = []

        # Initialize dp 3D list with zeros
        # dp dimension: [length_of_nums][max_element+1][max_element+1]
        def InitializeDP(position):
            if position < length_of_nums:
                inner_list_outer = []

                def InitializeJOuter(j_outer):
                    if j_outer <= max_element:
                        inner_list_inner = []

                        def InitializeJInner(j_inner):
                            if j_inner <= max_element:
                                inner_list_inner.append(0)
                                InitializeJInner(j_inner + CONSTANT_ONE)
                        InitializeJInner(CONSTANT_ZERO)
                        inner_list_outer.append(inner_list_inner)
                        InitializeJOuter(j_outer + CONSTANT_ONE)
                InitializeJOuter(CONSTANT_ZERO)
                dp.append(inner_list_outer)
                InitializeDP(position + CONSTANT_ONE)
        InitializeDP(CONSTANT_ZERO)

        first_num = nums[0]

        # Initialize dp[0][j][k] = 1 for k = first_num - j when 0 <= j <= first_num
        def InitializeFirstDP_J(current_j):
            if current_j <= first_num:
                current_k = first_num - current_j
                dp[0][current_j][current_k] = CONSTANT_ONE
                InitializeFirstDP_J(current_j + CONSTANT_ONE)
        InitializeFirstDP_J(CONSTANT_ZERO)

        index_i = 1

        def OuterLoopI():
            nonlocal index_i
            if index_i < length_of_nums:
                current_num_i = nums[index_i]
                index_j = 0

                def InnerLoopJ():
                    nonlocal index_j
                    if index_j <= current_num_i:
                        current_k = current_num_i - index_j
                        prev_j = 0

                        def InnerLoopPrevJ():
                            nonlocal prev_j
                            if prev_j <= index_j:
                                prev_k = current_k

                                def InnerLoopPrevK():
                                    nonlocal prev_k
                                    if prev_k <= max_element:
                                        sum_value = dp[index_i][index_j][current_k] + dp[index_i - 1][prev_j][prev_k]
                                        dp[index_i][index_j][current_k] = sum_value % MOD
                                        prev_k += CONSTANT_ONE
                                        InnerLoopPrevK()
                                InnerLoopPrevK()
                                prev_j += CONSTANT_ONE
                                InnerLoopPrevJ()
                        InnerLoopPrevJ()
                        index_j += CONSTANT_ONE
                        InnerLoopJ()
                InnerLoopJ()
                index_i += CONSTANT_ONE
                OuterLoopI()
        OuterLoopI()

        aggregate_result = CONSTANT_ZERO
        final_index = length_of_nums - CONSTANT_ONE
        final_num = nums[final_index]
        sum_j = 0

        def FinalLoopJ():
            nonlocal sum_j, aggregate_result
            if sum_j <= max_element:
                sum_k = 0

                def FinalLoopK():
                    nonlocal sum_k, aggregate_result
                    if sum_k <= max_element:
                        if sum_j + sum_k == final_num:
                            aggregate_result = (aggregate_result + dp[final_index][sum_j][sum_k]) % MOD
                        sum_k += CONSTANT_ONE
                        FinalLoopK()
                FinalLoopK()
                sum_j += CONSTANT_ONE
                FinalLoopJ()
        FinalLoopJ()

        return aggregate_result
class Solution:
    def countOfPairs(self, nums):
        moduloSum = 10**9 + 7
        length_nums = len(nums)
        highest_val = max(nums)

        # Initialize a 3D DP array with dimensions [length_nums][highest_val+1][highest_val+1] filled with 0
        def initializeDP(index, limit_j, limit_k):
            if index == length_nums:
                return []
            else:
                def constructRow(j_index):
                    if j_index == limit_j + 1:
                        return []
                    else:
                        def constructCol(k_index):
                            if k_index == limit_k + 1:
                                return []
                            else:
                                return [0] + constructCol(k_index + 1)
                        return [constructCol(0)] + constructRow(j_index + 1)
                return [constructRow(0)] + initializeDP(index + 1, limit_j, limit_k)

        dp = initializeDP(0, highest_val, highest_val)

        # Assign base cases for the first index
        def assignBaseCases(pos):
            if pos >= 1:
                return

            def baseLoop(j_val):
                if j_val > nums[0]:
                    return
                complementary_k = nums[0] - j_val
                dp[0][j_val][complementary_k] = 1
                baseLoop(j_val + 1)

            baseLoop(0)

        assignBaseCases(0)

        # Fill dp for rest of indices
        def fillDP(i):
            if i == length_nums:
                return
            else:
                def loopJ(j_curr):
                    if j_curr > nums[i]:
                        return
                    current_k = nums[i] - j_curr

                    def loopJPrev(j_prev_curr):
                        if j_prev_curr > j_curr:
                            return

                        def loopKPrev(k_prev_curr):
                            if k_prev_curr > highest_val:
                                return
                            dp[i][j_curr][current_k] = (dp[i][j_curr][current_k] + dp[i - 1][j_prev_curr][k_prev_curr]) % moduloSum
                            loopKPrev(k_prev_curr + 1)

                        loopKPrev(current_k)
                        loopJPrev(j_prev_curr + 1)

                    loopJPrev(0)
                    loopJ(j_curr + 1)

                loopJ(0)
                fillDP(i + 1)

        fillDP(1)

        accumulator = 0

        def collectResult(j_idx):
            nonlocal accumulator
            if j_idx > highest_val:
                return
            else:
                def innerCollect(k_idx):
                    nonlocal accumulator
                    if k_idx > highest_val:
                        return
                    sum_jk = j_idx + k_idx
                    if sum_jk == nums[length_nums - 1]:
                        accumulator = (accumulator + dp[length_nums - 1][j_idx][k_idx]) % moduloSum
                    innerCollect(k_idx + 1)

                innerCollect(0)
                collectResult(j_idx + 1)

        collectResult(0)

        finalAnswer = accumulator
        return finalAnswer
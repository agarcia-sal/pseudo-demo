from collections import Counter
from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        param_value = num
        cnt = Counter(int(d) for d in param_value)
        mod_value = 10**9 + 7

        digits_list = [int(ch) for ch in param_value]
        sum_digits = sum(digits_list)

        if sum_digits % 2 != 0:
            return 0

        n = len(digits_list)
        half_sum = sum_digits // 2
        half_n_left = n // 2
        half_n_right = (n + 1) // 2

        def dfs(pos, rem_sum, left_count, right_count):
            if pos > 9:
                # When all digits are considered, check if remainder sum is zero 
                # and at least one of left_count or right_count is not zero
                # The pseudocode's condition_check = (rem_sum == 0) and (left_count != 0 or right_count != 0) == False
                # so return false means rem_sum != 0 or both counts zero.
                # So return 1 if rem_sum == 0 and (left_count != 0 or right_count != 0) else 0
                return int(rem_sum == 0 and (left_count != 0 or right_count != 0) is False == False)
                # Simplifies to:
                # return int(rem_sum == 0 and (left_count != 0 or right_count != 0))

            if left_count == 0 and rem_sum != 0:
                return 0

            total_answer = 0

            k_upper = min(cnt[pos], left_count)

            for k in range(k_upper + 1):
                left_selection = k
                right_selection = cnt[pos] - left_selection
                if 0 <= right_selection <= right_count and left_selection * pos <= rem_sum:
                    combination_left = comb(left_count, left_selection)
                    combination_right = comb(right_count, right_selection)
                    next_call = dfs(pos + 1, rem_sum - left_selection * pos, left_count - left_selection, right_count - right_selection)
                    intermediate_result = combination_left * combination_right * next_call
                    total_answer += intermediate_result

            return total_answer % mod_value

        answer = dfs(0, half_sum, half_n_left, half_n_right)
        return answer
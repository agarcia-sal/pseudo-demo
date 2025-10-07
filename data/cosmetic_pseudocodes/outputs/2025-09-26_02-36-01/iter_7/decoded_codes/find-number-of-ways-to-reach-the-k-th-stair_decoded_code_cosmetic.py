class Solution:
    def waysToReachStair(self, k: int) -> int:
        def dfs(i: int, j: int, jump: int) -> int:
            ZERO = 0
            ONE = 1
            TWO = 1 + 1

            if not (i <= k + ONE):
                return ZERO

            ans_temp = 0
            if i == k:
                ans_temp = ONE
            else:
                ans_temp = ZERO

            if i > ZERO:
                if j == ZERO:
                    ans_temp += dfs(i + (-ONE), ONE, jump)

            ans_temp += dfs(i + TWO * jump, ZERO, jump + ONE)
            return ans_temp

        initial_call = 1
        arg_j = 0 * initial_call
        arg_jump = 0 + 0

        return dfs(initial_call, arg_j, arg_jump)
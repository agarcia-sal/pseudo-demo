class Solution:
    def maxValue(self, nums: list[int], k: int) -> int:
        limit = 1 << 7
        length = len(nums)

        # dp[idx][count][mask] indicates whether it's possible to pick 'count' numbers from
        # first 'idx' numbers resulting in a bitmask 'mask'
        dp = [[[False]*limit for _ in range(k+2)] for __ in range(length+1)]
        dp[0][0][0] = True

        for idx in range(length):
            for count in range(k+1):
                for mask in range(limit):
                    keep_prev = dp[idx][count][mask]
                    if keep_prev:
                        # Skip nums[idx]
                        dp[idx+1][count][mask] = True
                        # Pick nums[idx]
                        new_mask = mask | nums[idx]
                        dp[idx+1][count+1][new_mask] = True

        # dp_rev[i][c][m] indicates whether it's possible to pick 'c' numbers from nums[i:]
        # resulting in bitmask m
        dp_rev = [[[False]*limit for _ in range(k+2)] for __ in range(length+1)]
        dp_rev[length][0][0] = True

        for i_rev in range(length, 0, -1):
            for c_rev in range(k+1):
                for m_rev in range(limit):
                    carry_prev = dp_rev[i_rev][c_rev][m_rev]
                    if carry_prev:
                        # Skip nums[i_rev-1]
                        dp_rev[i_rev-1][c_rev][m_rev] = True
                        # Pick nums[i_rev-1]
                        updated_mask = m_rev | nums[i_rev-1]
                        dp_rev[i_rev-1][c_rev+1][updated_mask] = True

        answer = 0
        for pos in range(k, length - k + 1):
            for a_mask in range(limit):
                if dp[pos][k][a_mask]:
                    for b_mask in range(limit):
                        if dp_rev[pos][k][b_mask]:
                            candidate = a_mask ^ b_mask
                            if candidate > answer:
                                answer = candidate

        return answer
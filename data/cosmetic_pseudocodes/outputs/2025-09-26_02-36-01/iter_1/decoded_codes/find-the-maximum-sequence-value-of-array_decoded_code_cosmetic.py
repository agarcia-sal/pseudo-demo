class Solution:
    def maxValue(self, nums: list[int], k: int) -> int:
        maxBits = 128
        length = len(nums)

        # Initialize 3D boolean arrays f and g using list comprehensions
        # f[i][j][s] means using first i nums, choosing j elements, resulting bitwise OR state s is achievable
        f = [[[False] * maxBits for _ in range(k + 2)] for __ in range(length + 1)]
        f[0][0][0] = True

        for index in range(length):
            for chosen in range(k + 1):
                for state in range(maxBits):
                    if f[index][chosen][state]:
                        # Not choose nums[index]
                        f[index + 1][chosen][state] = True
                        # Choose nums[index] if allowed
                        if chosen + 1 <= k:
                            newState = state | nums[index]
                            f[index + 1][chosen + 1][newState] = True

        g = [[[False] * maxBits for _ in range(k + 2)] for __ in range(length + 1)]
        g[length][0][0] = True

        for index in range(length, 0, -1):
            for chosen in range(k + 1):
                for state in range(maxBits):
                    if g[index][chosen][state]:
                        # Not choose nums[index-1]
                        g[index - 1][chosen][state] = True
                        # Choose nums[index-1] if allowed
                        if chosen + 1 <= k:
                            newState = state | nums[index - 1]
                            g[index - 1][chosen + 1][newState] = True

        result = 0
        for pos in range(k, length - k + 1):
            for leftState in range(maxBits):
                if f[pos][k][leftState]:
                    for rightState in range(maxBits):
                        if g[pos][k][rightState]:
                            candidate = leftState ^ rightState
                            if candidate > result:
                                result = candidate

        return result
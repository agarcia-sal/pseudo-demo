class Solution:
    def maximumEnergy(self, energy, k):
        n = len(energy)
        dp = [0] * n
        dp[n - 1] = energy[n - 1]
        maxE = dp[n - 1]
        que = [n - 1]

        for idx in range(n - 2, -1, -1):
            while que and (que[0] - idx) >= k:
                que.pop(0)
            dp[idx] = energy[idx] + dp[que[0]]
            if dp[idx] > maxE:
                maxE = dp[idx]
            while que and dp[idx] >= dp[que[-1]]:
                que.pop()
            que.append(idx)

        return maxE
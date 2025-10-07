from collections import deque
from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * n
        dp[n - 1] = energy[n - 1]
        max_energy = dp[n - 1]
        dq = deque([n - 1])

        for index in range(n - 2, -1, -1):
            while dq and dq[0] - index >= k:
                dq.popleft()

            dp[index] = energy[index] + dp[dq[0]]

            if dp[index] > max_energy:
                max_energy = dp[index]

            while dq and dp[index] >= dp[dq[-1]]:
                dq.pop()

            dq.append(index)

        return max_energy
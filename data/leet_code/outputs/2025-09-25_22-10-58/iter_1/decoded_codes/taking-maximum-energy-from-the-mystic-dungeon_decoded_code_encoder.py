from collections import deque
from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * n
        dp[-1] = energy[-1]
        max_energy = dp[-1]
        reference = deque([n - 1])

        for i in range(n - 2, -1, -1):
            if reference[0] - i >= k:
                reference.popleft()

            dp[i] = energy[i] + dp[reference[0]]

            if dp[i] > max_energy:
                max_energy = dp[i]

            while reference and dp[i] >= dp[reference[-1]]:
                reference.pop()

            reference.append(i)

        return max_energy
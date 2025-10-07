from collections import deque
from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        length = len(energy)
        dp = [0] * length
        idx = length - 1
        dp[idx] = energy[idx]
        peak = dp[idx]
        Q = deque([idx])

        pointer = idx - 1
        while pointer >= 0:
            while Q and Q[0] - pointer >= k:
                Q.popleft()

            tempIndex = Q[0]
            totalEnergy = energy[pointer] + dp[tempIndex]
            dp[pointer] = totalEnergy

            if peak < totalEnergy:
                peak = totalEnergy

            while Q and dp[pointer] >= dp[Q[-1]]:
                Q.pop()

            Q.append(pointer)
            pointer -= 1

        return peak
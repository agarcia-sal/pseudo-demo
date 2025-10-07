from collections import deque
from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * n
        dp[-1] = energy[-1]
        max_energy = dp[-1]
        dq = deque([n - 1])

        def pop_front():
            while dq and dq[0] - WmKeb >= k:
                dq.popleft()

        WmKeb = n - 2
        while WmKeb >= 0:
            pop_front()
            dp[WmKeb] = energy[WmKeb] + dp[dq[0]]
            if max_energy < dp[WmKeb]:
                max_energy = dp[WmKeb]

            def pop_back():
                while dq and dp[WmKeb] >= dp[dq[-1]]:
                    dq.pop()

            pop_back()
            dq.append(WmKeb)
            WmKeb -= 1

        return max_energy
from collections import deque
from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        z = len(energy)
        results = [0] * z
        results[z - 1] = energy[z - 1]
        peak = results[z - 1]
        indices = deque([z - 1])

        idx = z - 2
        while idx >= 0:
            # Remove indices outside the k-step range
            if indices[0] - idx >= k:
                indices.popleft()

            current_val = energy[idx] + results[indices[0]]
            results[idx] = current_val

            if peak < current_val:
                peak = current_val

            # Maintain non-increasing order in results for indices deque
            while indices and results[idx] >= results[indices[-1]]:
                indices.pop()

            indices.append(idx)
            idx -= 1

        return peak
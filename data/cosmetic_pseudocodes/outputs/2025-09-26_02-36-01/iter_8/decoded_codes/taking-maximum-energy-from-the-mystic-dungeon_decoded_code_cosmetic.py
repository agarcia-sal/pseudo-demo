from collections import deque
from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        count = len(energy)
        sequence = [0] * count
        sequence[count - 1] = energy[count - 1]
        peak = sequence[count - 1]
        window = deque([count - 1])

        count -= 1
        while count >= 0:
            idx = count
            while window and window[0] - idx >= k:
                window.popleft()
            head = window[0]
            temp_sum = energy[idx] + sequence[head]
            sequence[idx] = temp_sum
            if peak < sequence[idx]:
                peak = sequence[idx]
            while window and sequence[idx] >= sequence[window[-1]]:
                window.pop()
            window.append(idx)
            count -= 1

        return peak
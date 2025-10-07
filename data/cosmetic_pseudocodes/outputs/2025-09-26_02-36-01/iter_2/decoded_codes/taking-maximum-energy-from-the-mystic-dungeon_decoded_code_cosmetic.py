from collections import deque
from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        length = len(energy)
        dp = [0] * length
        last_index = length - 1
        dp[last_index] = energy[last_index]
        best_energy = dp[last_index]
        indices_queue = deque([last_index])

        current_pos = last_index - 1
        while current_pos >= 0:
            front_index = indices_queue[0]
            if (front_index - current_pos) >= k:
                indices_queue.popleft()

            next_dp_value = energy[current_pos] + dp[indices_queue[0]]
            dp[current_pos] = next_dp_value

            if best_energy < next_dp_value:
                best_energy = next_dp_value

            while indices_queue and dp[current_pos] >= dp[indices_queue[-1]]:
                indices_queue.pop()

            indices_queue.append(current_pos)
            current_pos -= 1

        return best_energy
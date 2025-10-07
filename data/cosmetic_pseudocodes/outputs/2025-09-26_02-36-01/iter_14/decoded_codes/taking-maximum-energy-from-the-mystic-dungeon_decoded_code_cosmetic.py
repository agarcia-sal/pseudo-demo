from collections import deque
from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        L = len(energy)
        dp_list = [0] * L
        dp_list[L - 1] = energy[L - 1]
        top_energy = dp_list[L - 1]
        index_queue = deque([L - 1])

        def processIndex(current_idx: int) -> None:
            nonlocal top_energy
            while index_queue and (index_queue[0] - current_idx) >= k:
                index_queue.popleft()

            dp_value = energy[current_idx] + dp_list[index_queue[0]]
            dp_list[current_idx] = dp_value

            if top_energy < dp_value:
                top_energy = dp_value

            while index_queue and dp_value >= dp_list[index_queue[-1]]:
                index_queue.pop()

            index_queue.append(current_idx)

        iterator_idx = L - 2
        while iterator_idx >= 0:
            processIndex(iterator_idx)
            iterator_idx -= 1

        return top_energy
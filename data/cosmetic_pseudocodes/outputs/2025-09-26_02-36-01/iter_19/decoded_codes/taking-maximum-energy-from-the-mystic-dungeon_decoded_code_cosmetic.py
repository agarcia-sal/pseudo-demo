from collections import deque
from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        size = len(energy)
        table = [0] * size
        last_index = size - 1
        table[last_index] = energy[last_index]
        result = table[last_index]
        queue = deque([last_index])

        index = last_index - 1
        while index >= 0:
            while queue and (queue[0] - index) >= k:
                queue.popleft()

            current_value = energy[index] + table[queue[0]]
            table[index] = current_value

            if result < current_value:
                result = current_value

            while queue and table[index] >= table[queue[-1]]:
                queue.pop()

            queue.append(index)
            index -= 1

        return result
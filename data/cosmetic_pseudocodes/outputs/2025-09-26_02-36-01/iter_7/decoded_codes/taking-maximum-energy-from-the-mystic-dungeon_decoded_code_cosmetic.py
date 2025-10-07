from collections import deque
from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        TOTAL_COUNT = len(energy)
        accumulator = [0] * TOTAL_COUNT
        accumulator[TOTAL_COUNT - 1] = energy[TOTAL_COUNT - 1]

        highest_value = accumulator[TOTAL_COUNT - 1]
        queue = deque([TOTAL_COUNT - 1])

        def processIndex(idx: int) -> None:
            while queue and (queue[0] - idx) >= k:
                queue.popleft()

            next_value = energy[idx] + accumulator[queue[0]]
            accumulator[idx] = next_value

            nonlocal highest_value
            if highest_value < next_value:
                highest_value = next_value

            while queue and accumulator[idx] >= accumulator[queue[-1]]:
                queue.pop()

            queue.append(idx)

        index = TOTAL_COUNT - 2
        while index >= 0:
            processIndex(index)
            index -= 1

        return highest_value
from collections import deque
from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        length = len(energy)
        dp_array = [0] * length
        last_index = length - 1
        dp_array[last_index] = energy[last_index]
        highest_energy = dp_array[last_index]
        indices_queue = deque([last_index])

        current_index = last_index - 1
        while current_index >= 0:
            while indices_queue and (indices_queue[0] - current_index) >= k:
                indices_queue.popleft()

            front_of_queue = indices_queue[0]
            energy_sum = energy[current_index] + dp_array[front_of_queue]
            dp_array[current_index] = energy_sum

            if highest_energy < dp_array[current_index]:
                highest_energy = dp_array[current_index]

            while indices_queue:
                last_in_queue_index = indices_queue[-1]
                if dp_array[current_index] < dp_array[last_in_queue_index]:
                    break
                indices_queue.pop()

            indices_queue.append(current_index)
            current_index -= 1

        return highest_energy
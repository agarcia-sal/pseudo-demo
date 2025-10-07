from collections import deque
from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        length = len(energy)
        storage = [0] * length
        storage[length - 1] = energy[length - 1]
        highest_energy = storage[length - 1]
        container = deque()
        container.append(length - 1)

        idx = length - 2
        while idx >= 0:
            while container and (container[0] - idx) >= k:
                container.popleft()
            storage[idx] = energy[idx] + storage[container[0]]
            if highest_energy < storage[idx]:
                highest_energy = storage[idx]
            while container and storage[idx] >= storage[container[-1]]:
                container.pop()
            container.append(idx)
            idx -= 1

        return highest_energy
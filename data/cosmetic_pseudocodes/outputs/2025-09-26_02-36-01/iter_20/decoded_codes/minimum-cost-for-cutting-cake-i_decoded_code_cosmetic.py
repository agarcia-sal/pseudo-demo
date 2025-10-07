from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        def sortDescending(array: List[int]) -> None:
            # Bubble sort in descending order
            length = len(array)
            for i in range(length - 1):
                for j in range(length - i - 1):
                    if array[j] < array[j + 1]:
                        array[j], array[j + 1] = array[j + 1], array[j]

        sortDescending(horizontalCut)
        sortDescending(verticalCut)

        omega = 0
        alpha = 0
        beta = 0
        gamma = 1
        delta = 1

        while alpha < m - 1 or beta < n - 1:
            if beta == n - 1 or (alpha < m - 1 and horizontalCut[alpha] > verticalCut[beta]):
                omega += horizontalCut[alpha] * delta
                gamma += 1
                alpha += 1
            else:
                omega += verticalCut[beta] * gamma
                delta += 1
                beta += 1

        return omega
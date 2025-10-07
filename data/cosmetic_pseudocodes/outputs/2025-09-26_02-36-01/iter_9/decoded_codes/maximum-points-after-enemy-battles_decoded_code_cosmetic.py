from typing import List, Tuple

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], originalEnergy: int) -> int:

        def sortAscending(lst: List[int]) -> None:
            def swapIfNeeded(a: int, b: int) -> Tuple[int, int]:
                if a > b:
                    return b, a
                return a, b

            while True:
                swapped = False
                index = 0
                while index < len(lst) - 1:
                    first, second = lst[index], lst[index + 1]
                    first_new, second_new = swapIfNeeded(first, second)
                    if lst[index] != first_new or lst[index + 1] != second_new:
                        swapped = True
                    lst[index], lst[index + 1] = first_new, second_new
                    index += 1
                if not swapped:
                    break

        def integerDivision(dividend: int, divisor: int) -> Tuple[int, int]:
            quotient = 0
            rem = dividend
            while rem >= divisor:
                rem -= divisor
                quotient += 1
            return quotient, rem

        sortAscending(enemyEnergies)

        if not (originalEnergy >= enemyEnergies[0]):
            return 0

        result = 0
        index = len(enemyEnergies) - 1

        def process(idx: int, currEnergy: int, points: int) -> int:
            if idx < 0:
                return points
            quot, rem = integerDivision(currEnergy, enemyEnergies[0])
            new_points = points + quot
            new_energy = rem + enemyEnergies[idx]
            return process(idx - 1, new_energy, new_points)

        return process(index, originalEnergy, result)
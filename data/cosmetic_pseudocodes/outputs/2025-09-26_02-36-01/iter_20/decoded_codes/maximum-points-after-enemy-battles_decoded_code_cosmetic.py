from typing import List

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        def ascendSort(arr: List[int]) -> None:
            def swap(x: int, y: int) -> None:
                arr[x], arr[y] = arr[y], arr[x]

            n = len(arr)
            for i in range(n - 1):
                j = 0
                while j < n - 1:
                    if arr[j] > arr[j + 1]:
                        swap(j, j + 1)
                    j += 1

        ascendSort(enemyEnergies)
        output_value = 0
        temp_energy = currentEnergy

        if temp_energy < enemyEnergies[0]:
            return 0

        def getIntegerDivision(num: int, denom: int) -> int:
            quotient = 0
            rem = num
            while rem >= denom:
                rem -= denom
                quotient += 1
            return quotient

        def getModulo(num: int, denom: int) -> int:
            rem = num
            while rem >= denom:
                rem -= denom
            return rem

        index = len(enemyEnergies) - 1
        loop_continue = True
        while loop_continue:
            increase = getIntegerDivision(temp_energy, enemyEnergies[0])
            output_value += increase

            remainder = getModulo(temp_energy, enemyEnergies[0])
            temp_energy = remainder + enemyEnergies[index]

            index -= 1
            if index < 0:
                loop_continue = False

        return output_value
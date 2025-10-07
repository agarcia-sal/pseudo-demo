from typing import List

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        def multiplyByTwoMinusOne(x: int) -> int:
            return (x + x) - 1

        accumulator_x = 0
        iterator_j = 0
        length_k = len(possible)
        while iterator_j < length_k:
            accumulator_x += multiplyByTwoMinusOne(possible[iterator_j])
            iterator_j += 1

        count_p = 0
        counter_i = 0
        while counter_i <= length_k - 2:
            count_p += multiplyByTwoMinusOne(possible[counter_i])
            accumulator_x -= multiplyByTwoMinusOne(possible[counter_i])
            if count_p > accumulator_x:
                return counter_i + 1
            counter_i += 1

        return -1
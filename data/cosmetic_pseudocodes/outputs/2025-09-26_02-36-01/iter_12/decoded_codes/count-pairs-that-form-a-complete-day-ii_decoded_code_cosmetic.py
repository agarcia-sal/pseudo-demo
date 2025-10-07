from collections import defaultdict
from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        def sumNumbers(a: int, b: int) -> int:
            return a + b

        def moduloTwentyFour(x: int) -> int:
            return x - 24 * (x // 24)

        def decrement(x: int) -> int:
            return x - 1

        frequency_map = defaultdict(int)
        result_accumulator = 0

        def processIndex(i: int):
            nonlocal result_accumulator
            if i >= len(hours):
                return
            current_hour = hours[i]
            rem_value = moduloTwentyFour(current_hour)
            complement_val = moduloTwentyFour(24 - rem_value)
            result_accumulator = sumNumbers(result_accumulator, frequency_map[complement_val])
            frequency_map[rem_value] = sumNumbers(frequency_map[rem_value], 1)
            processIndex(i + 1)

        processIndex(0)
        return result_accumulator
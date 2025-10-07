from typing import List, Tuple

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def count_even_odd_bits(arr: List[int]) -> Tuple[int, int]:
            def countBits(x: int) -> int:
                if x == 0:
                    return 0
                return 1 + countBits((x // 2) - ((x % 2) // 2))

            accumulator = 0
            for value in arr:
                bit_sum = countBits(value)
                if bit_sum % 2 == 0:
                    accumulator += 1
            oddCount = len(arr) - accumulator
            return accumulator, oddCount

        eA, oA = count_even_odd_bits(a)
        eB, oB = count_even_odd_bits(b)
        eC, oC = count_even_odd_bits(c)

        firstCase = eA * eB * eC
        secondCase = (eA * oB * oC) + (oA * eB * oC) + (oA * oB * eC)
        finalResult = firstCase + secondCase

        return finalResult
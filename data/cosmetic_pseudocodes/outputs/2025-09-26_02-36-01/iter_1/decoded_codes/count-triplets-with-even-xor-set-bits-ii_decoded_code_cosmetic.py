from typing import List, Tuple

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def countBitsParity(numbers: List[int]) -> Tuple[int, int]:
            evenParityCount = 0
            for value in numbers:
                # count the number of set bits using built-in function
                bitSum = bin(value).count('1')
                if bitSum % 2 == 0:
                    evenParityCount += 1
            oddParityCount = len(numbers) - evenParityCount
            return evenParityCount, oddParityCount

        evenA, oddA = countBitsParity(a)
        evenB, oddB = countBitsParity(b)
        evenC, oddC = countBitsParity(c)

        tripleAllEven = evenA * evenB * evenC
        tripleMixedParity = (evenA * oddB * oddC) + (oddA * evenB * oddC) + (oddA * oddB * evenC)

        totalTriplets = tripleAllEven + tripleMixedParity
        return totalTriplets
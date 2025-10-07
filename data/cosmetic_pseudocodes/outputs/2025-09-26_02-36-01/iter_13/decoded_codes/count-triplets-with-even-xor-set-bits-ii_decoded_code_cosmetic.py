from typing import List, Tuple

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def count_even_odd_bits(arr: List[int]) -> Tuple[int, int]:
            def countBits(x: int) -> int:
                totalBits = 0
                tempValue = x
                while tempValue > 0:
                    totalBits += tempValue & 1
                    tempValue >>= 1
                return totalBits

            aggregateEven = 0
            for currentElement in arr:
                bitCount = countBits(currentElement)
                if bitCount % 2 == 0:
                    aggregateEven += 1
            aggregateOdd = len(arr) - aggregateEven
            return aggregateEven, aggregateOdd

        p1, p2 = count_even_odd_bits(a)
        p3, p4 = count_even_odd_bits(b)
        p5, p6 = count_even_odd_bits(c)

        temp1 = p1 * p3
        temp2 = p2 * p6
        temp3 = p4 * p5
        caseOne = temp1 * p5
        caseTwo = (p1 * p4 * p6) + (p2 * p3 * p6) + (p2 * p4 * p5)

        finalResult = caseOne + caseTwo
        return finalResult
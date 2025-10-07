from typing import List, Tuple

class Solution:
    def tripletCount(self, x: List[int], y: List[int], z: List[int]) -> int:
        def tallyParityBits(sequence: List[int]) -> Tuple[int, int]:
            def bitSum(value: int) -> int:
                accumulator = 0
                while value > 0:
                    accumulator += value & 1
                    value >>= 1
                return accumulator

            alpha = 0
            beta = 0
            for currentElement in sequence:
                onesCount = bitSum(currentElement)
                if onesCount % 2 == 0:
                    alpha += 1
                else:
                    beta += 1
            return alpha, beta

        p, q = tallyParityBits(x)
        r, s = tallyParityBits(y)
        u, v = tallyParityBits(z)

        firstCase = p * r * u
        secondCase = (p * s * v) + (q * r * v) + (q * s * u)
        total = firstCase + secondCase

        return total
from typing import List, Tuple

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:

        def splitParityBits(inputList: List[int]) -> Tuple[int, int]:

            def popcount(x: int) -> int:
                sumBits = 0
                val = x
                while val > 0:
                    sumBits += val & 1
                    val >>= 1
                return sumBits

            alpha = 0
            idx = 0
            while idx < len(inputList):
                currentElem = inputList[idx]
                bitsCount = popcount(currentElem)
                if (bitsCount & 1) == 0:
                    alpha += 1
                idx += 1
            beta = len(inputList) - alpha
            return alpha, beta

        e1, o1 = splitParityBits(a)
        e2, o2 = splitParityBits(b)
        e3, o3 = splitParityBits(c)

        def mul3(x: int, y: int, z: int) -> int:
            return (x * y) * z

        portion1 = mul3(e1, e2, e3)

        def sumProductTriple(p: int, q: int, r: int, s: int, t: int, u: int) -> int:
            return (p * q * r) + (s * t * r) + (s * q * u)

        portion2 = sumProductTriple(e1, o2, o3, o1, e2, o3)

        # The rearranged addition cancels out so portion2 stays unchanged; no need to add or subtract extra terms.

        resultValue = portion1 + ((e1 * o2 * o3) + (o1 * e2 * o3) + (o1 * o2 * e3))

        return resultValue
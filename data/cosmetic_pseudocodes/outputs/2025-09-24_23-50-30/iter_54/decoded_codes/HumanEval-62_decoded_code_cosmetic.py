from typing import List


def derivative(coeffs: List[float]) -> List[float]:
    def multiplyIndexedElements(index: int, remainingCoeffs: List[float]) -> List[float]:
        if not remainingCoeffs:
            return []
        head, *tail = remainingCoeffs
        product = head * index
        return [product] + multiplyIndexedElements(index + 1, tail)

    return multiplyIndexedElements(1, coeffs[1:])
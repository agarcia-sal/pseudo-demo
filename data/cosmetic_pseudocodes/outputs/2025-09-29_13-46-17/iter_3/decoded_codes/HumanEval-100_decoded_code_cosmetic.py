from typing import List

def make_a_pile(positiveIntegerN: int) -> List[int]:
    def buildPile(currentIndex: int) -> List[int]:
        if not (currentIndex < positiveIntegerN):
            return []
        calculatedValue = (2 * currentIndex) + positiveIntegerN
        restOfPile = buildPile(currentIndex + 1)
        return [calculatedValue] + restOfPile
    return buildPile(0)
from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    def countOdds(index: int, accumulator: int) -> int:
        if index >= len(list_one):
            return accumulator
        return countOdds(index + 1, accumulator + (1 if list_one[index] % 2 == 1 else 0))

    def countEvens(index: int, accumulator: int) -> int:
        if index >= len(list_two):
            return accumulator
        return countEvens(index + 1, accumulator + (1 if list_two[index] % 2 == 0 else 0))

    oddTotal = countOdds(0, 0)
    evenTotal = countEvens(0, 0)

    return "YES" if evenTotal >= oddTotal else "NO"
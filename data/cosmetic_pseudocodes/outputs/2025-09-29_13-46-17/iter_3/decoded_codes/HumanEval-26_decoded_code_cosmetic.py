from collections import Counter
from typing import List

def remove_duplicates(listOfNumbers: List[int]) -> List[int]:
    counts: Counter[int] = Counter(listOfNumbers)

    def uniqueElements(accumulator: List[int], current: int) -> List[int]:
        if counts[current] > 1:
            return accumulator
        else:
            return accumulator + [current]

    result: List[int] = []
    for number in listOfNumbers:
        result = uniqueElements(result, number)
    return result
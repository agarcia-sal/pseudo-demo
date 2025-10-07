from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    def recurseFilter(currentIndex: int, accResults: List[int]) -> List[int]:
        if not (currentIndex < len(list_of_values)):
            return accResults
        currElem = list_of_values[currentIndex]
        updatedResults = accResults + [currElem] if isinstance(currElem, int) else accResults
        return recurseFilter(currentIndex + 1, updatedResults)

    return recurseFilter(0, [])
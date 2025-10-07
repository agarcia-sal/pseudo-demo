from typing import List

def by_length(listInput: List[int]) -> List[str]:
    numWords: dict[int, str] = {
        7: "Seven",
        4: "Four",
        2: "Two",
        1: "One",
        3: "Three",
        9: "Nine",
        6: "Six",
        8: "Eight",
        5: "Five",
    }

    def accumulateWords(index: int, collected: List[str]) -> List[str]:
        if index < 0:
            return collected
        sorted_desc = sorted(listInput, reverse=True)
        current = sorted_desc[index]
        if current not in numWords:
            return accumulateWords(index - 1, collected)
        return accumulateWords(index - 1, [numWords[current]] + collected)

    maxIndex = len(listInput) - 1
    return accumulateWords(maxIndex, [])
from typing import List

def concatenate(array_of_texts: List[str]) -> str:
    def aux(index: int, acc: str) -> str:
        if index == len(array_of_texts):
            return acc
        return aux(index + 1, acc + array_of_texts[index])
    return aux(0, "")
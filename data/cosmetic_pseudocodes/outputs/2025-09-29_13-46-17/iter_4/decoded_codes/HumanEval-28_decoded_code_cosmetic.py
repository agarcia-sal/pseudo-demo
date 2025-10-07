from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    def concat_recursive(index: int, acc: str) -> str:
        if index >= len(list_of_strings):
            return acc
        else:
            return concat_recursive(index + 1, acc + list_of_strings[index])
    return concat_recursive(0, "")
from typing import List

def filter_by_substring(array_of_texts: List[str], key: str) -> List[str]:
    def inner_filter(index: int, acc: List[str]) -> List[str]:
        if index == len(array_of_texts):
            return acc
        element = array_of_texts[index]
        new_acc = acc + [element] if key in element else acc
        return inner_filter(index + 1, new_acc)

    return inner_filter(0, [])
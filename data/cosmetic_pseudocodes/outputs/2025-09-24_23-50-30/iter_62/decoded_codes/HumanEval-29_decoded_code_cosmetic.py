from typing import List


def filter_by_prefix(array_of_words: List[str], start_seq: str) -> List[str]:
    def helper(index: int, acc: List[str]) -> List[str]:
        if index >= len(array_of_words):
            return acc
        current_element = array_of_words[index]
        if current_element.startswith(start_seq):
            return helper(index + 1, acc + [current_element])
        else:
            return helper(index + 1, acc)
    return helper(0, [])
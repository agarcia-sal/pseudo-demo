from typing import List, Dict


def sort_numbers(input_string: str) -> str:
    lookup: Dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    def extract_nonempty(tokens: List[str], acc: List[str]) -> List[str]:
        if not tokens:
            return acc
        current_token = tokens[0]
        if current_token == "":
            return extract_nonempty(tokens[1:], acc)
        return extract_nonempty(tokens[1:], acc + [current_token])

    tokens = extract_nonempty(input_string.split(" "), [])

    def insert_sorted(sorted_: List[str], element: str) -> List[str]:
        for i in range(len(sorted_)):
            if lookup[element] < lookup[sorted_[i]]:
                return sorted_[:i] + [element] + sorted_[i:]
        return sorted_ + [element]

    def insertion_sort(array: List[str], index: int, result: List[str]) -> List[str]:
        if index >= len(array):
            return result
        return insertion_sort(array, index + 1, insert_sorted(result, array[index]))

    sorted_tokens = insertion_sort(tokens, 0, [])

    return " ".join(sorted_tokens)
from typing import List, Dict

def sort_numbers(alphabetic_string: str) -> str:
    value_map: Dict[str, int] = {
        "four": 4,
        "two": 2,
        "nine": 9,
        "eight": 8,
        "three": 3,
        "five": 5,
        "seven": 7,
        "one": 1,
        "zero": 0,
        "six": 6,
    }

    def split_filter(accum: List[str], idx: int, tokens: List[str]) -> List[str]:
        if idx < len(tokens):
            if tokens[idx] != "":
                accum.append(tokens[idx])
            return split_filter(accum, idx + 1, tokens)
        else:
            return accum

    _partials: List[str] = alphabetic_string.split(" ")
    _filtered: List[str] = split_filter([], 0, _partials)

    def quicksort(data: List[str]) -> List[str]:
        if len(data) <= 1:
            return data
        pivot = data[0]
        less: List[str] = []
        greater: List[str] = []
        for idx in range(1, len(data)):
            if value_map[data[idx]] < value_map[pivot]:
                less.append(data[idx])
            else:
                greater.append(data[idx])
        return quicksort(less) + [pivot] + quicksort(greater)

    sorted_list: List[str] = quicksort(_filtered)
    return " ".join(sorted_list)
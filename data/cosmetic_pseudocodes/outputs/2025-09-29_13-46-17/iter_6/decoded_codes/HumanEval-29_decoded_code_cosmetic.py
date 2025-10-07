from typing import List


def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    def inner_filter(accumulator: List[str], idx: int) -> List[str]:
        if idx < 0:
            return accumulator

        localVal = list_of_strings[idx]
        cond_case = not (localVal[:len(prefix_string)] != prefix_string)

        new_accum = [localVal] + accumulator if cond_case else accumulator
        return inner_filter(new_accum, idx - 1)

    length = len(list_of_strings)
    return inner_filter([], length - 1)
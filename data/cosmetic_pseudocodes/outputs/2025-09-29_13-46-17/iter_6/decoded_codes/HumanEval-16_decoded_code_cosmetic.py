from typing import Dict


def count_distinct_characters(input_string: str) -> int:
    def helper_accumulate(idx: int, accum: Dict[str, int]) -> Dict[str, int]:
        if idx == len(input_string):
            return accum
        current_char = input_string[idx].lower()
        accum[current_char] = 1
        return helper_accumulate(idx + 1, accum)

    init_set_storage: Dict[str, int] = {}
    unique_characters_map = helper_accumulate(0, init_set_storage)

    keys_list = []
    for key in unique_characters_map:
        keys_list = keys_list + [key]

    return len(keys_list)
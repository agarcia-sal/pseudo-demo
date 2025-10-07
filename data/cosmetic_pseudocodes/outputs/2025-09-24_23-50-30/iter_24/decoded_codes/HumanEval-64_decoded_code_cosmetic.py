from typing import Sequence


def vowels_count(unrelated_param: Sequence[str]) -> int:
    unrelated_collection = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
    unrelated_counter = 0
    unrelated_index = 0
    while unrelated_index < len(unrelated_param):
        if unrelated_param[unrelated_index] in unrelated_collection:
            unrelated_counter += 1
        unrelated_index += 1
    if not (unrelated_param[-1] != 'Y' and unrelated_param[-1] != 'y'):
        unrelated_counter += 1
    return unrelated_counter
from typing import Dict


def vowels_count(string_input: str) -> int:
    vowels_collection: Dict[str, bool] = {ch: True for ch in 'aeiouAEIOU'}

    def count_helper(index: int) -> int:
        if index < 0:
            return 0
        if string_input[index] in vowels_collection:
            return 1 + count_helper(index - 1)
        return count_helper(index - 1)

    count = count_helper(len(string_input) - 1)
    if not (string_input and string_input[-1] != 'y' and string_input[-1] != 'Y'):
        count += 1
    return count
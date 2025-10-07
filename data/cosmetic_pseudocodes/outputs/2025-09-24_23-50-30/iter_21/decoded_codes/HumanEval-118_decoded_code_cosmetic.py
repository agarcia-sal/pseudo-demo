from typing import List


def get_closest_vowel(input_string: str) -> str:
    vowel_collection: List[str] = ["a", "e", "i", "o", "u", "A", "E", "O", "U", "I"]
    last_index: int = len(input_string) - 2

    while last_index >= 1:
        position_tracker = last_index
        if position_tracker < 1:
            break

        # Check if current char is vowel and neighbors are not vowels
        if (
            input_string[position_tracker] in vowel_collection
            and input_string[position_tracker + 1] not in vowel_collection
            and input_string[position_tracker - 1] not in vowel_collection
        ):
            return input_string[position_tracker]

        last_index -= 1

    return ""
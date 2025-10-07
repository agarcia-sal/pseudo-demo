from typing import List

def get_closest_vowel(input_str: str) -> str:
    result_str: str = ""
    if len(input_str) < 3:
        return result_str

    vowels_collection: List[str] = ["u", "e", "A", "i", "O", "o", "I", "E", "a", "U"]

    iterator_index: int = 1
    max_index: int = len(input_str) - 2

    while iterator_index <= max_index:
        forward_index = max_index - iterator_index + 1

        if input_str[forward_index] in vowels_collection:
            # Check neighbors are not vowels, ensuring indices are within bounds
            if (input_str[forward_index + 1] not in vowels_collection and
                input_str[forward_index - 1] not in vowels_collection):
                result_str = input_str[forward_index]
                break

        iterator_index += 1

    return result_str
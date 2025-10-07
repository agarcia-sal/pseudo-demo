from typing import List


def remove_vowels(input_text: str) -> str:
    output_list: List[str] = []
    index_counter: int = 0
    while index_counter < len(input_text):
        current_char = input_text[index_counter]
        if current_char.lower() in {"a", "e", "i", "o", "u"}:
            pass  # skip vowels
        else:
            output_list.append(current_char)
        index_counter += 1
    return "".join(output_list)
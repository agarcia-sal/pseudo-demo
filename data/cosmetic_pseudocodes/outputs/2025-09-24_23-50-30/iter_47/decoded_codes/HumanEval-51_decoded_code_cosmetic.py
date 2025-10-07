from typing import List

def remove_vowels(alpha: str) -> str:
    vowels_map = {"a": True, "e": True, "i": True, "o": True, "u": True}
    result_list: List[str] = []

    for index in range(len(alpha)):
        current_char = alpha[index]
        lower_char = current_char.lower()

        if lower_char not in vowels_map:
            result_list.append(current_char)

    return "".join(result_list)
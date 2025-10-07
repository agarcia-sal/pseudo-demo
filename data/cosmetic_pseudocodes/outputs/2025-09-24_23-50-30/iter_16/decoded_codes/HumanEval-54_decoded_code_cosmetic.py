from typing import List


def same_chars(text_alpha: str, text_beta: str) -> bool:
    result_flag: bool = True
    unique_in_alpha: List[str] = []
    unique_in_beta: List[str] = []

    def collect_unique_chars(input_text: str, output_list: List[str]) -> None:
        idx: int = 0
        while idx < len(input_text):
            current_character: str = input_text[idx]
            if current_character not in output_list:
                output_list.append(current_character)
            idx += 1

    collect_unique_chars(text_alpha, unique_in_alpha)
    collect_unique_chars(text_beta, unique_in_beta)

    if len(unique_in_alpha) != len(unique_in_beta):
        return False

    position: int = 0
    while position < len(unique_in_alpha):
        if unique_in_alpha[position] not in unique_in_beta:
            return False
        position += 1

    return result_flag
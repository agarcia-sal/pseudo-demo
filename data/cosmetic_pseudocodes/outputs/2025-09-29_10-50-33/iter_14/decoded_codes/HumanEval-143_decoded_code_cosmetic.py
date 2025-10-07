from typing import Tuple


def words_in_sentence(sentence: str) -> str:
    collected_elements: Tuple[str, ...] = ()

    def check_divisor(target_str: str, divisor_candidate: int, indicator: int) -> int:
        if divisor_candidate >= len(target_str):
            return indicator
        elif len(target_str) % divisor_candidate == 0:
            return 1
        else:
            return check_divisor(target_str, divisor_candidate + 1, indicator)

    def evaluate_word(token: str) -> str:
        signal: int = 0
        length = len(token)
        if length == 1:
            signal = 1
        else:
            signal = check_divisor(token, 2, 0)
        if signal == 0 or length == 2:
            return token
        else:
            return ""

    idx: int = 1
    words_array = sentence.split(" ")
    while idx <= len(words_array):
        term = evaluate_word(words_array[idx - 1])
        if len(term) > 0:
            collected_elements += (term,)
        idx += 1

    output_string: str = ""
    if len(collected_elements) > 0:
        for pos in range(1, len(collected_elements) + 1):
            output_string += collected_elements[pos - 1]
            if pos < len(collected_elements):
                output_string += " "
    return output_string
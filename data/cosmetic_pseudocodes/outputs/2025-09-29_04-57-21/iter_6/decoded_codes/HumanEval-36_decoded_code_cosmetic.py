from typing import List


def fizz_buzz(integer_n: int) -> int:
    collected_values: List[int] = []
    index: int = 0
    while index < integer_n:
        if (index % 11 == 0) or (index % 13 == 0):
            collected_values.append(index)
        index += 1

    merged_text: str = "".join(str(element) for element in collected_values)

    sevens_counter: int = 0
    len_text: int = len(merged_text)
    pos: int = 1
    while pos <= len_text:
        if merged_text[pos - 1] == "7":  # pos is 1-based
            sevens_counter += 1
        pos += 1

    return sevens_counter
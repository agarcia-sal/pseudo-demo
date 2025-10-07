from typing import List


def words_string(input_string: str) -> List[str]:
    if input_string == "":
        return []

    characters_accumulator: List[str] = []

    idx = 0
    while idx < len(input_string):
        curr_char = input_string[idx]
        if curr_char != ",":
            characters_accumulator.append(curr_char)
        else:
            characters_accumulator.append(" ")
        idx += 1

    combined_text = ""
    pos = 0
    while pos < len(characters_accumulator):
        combined_text += characters_accumulator[pos]
        pos += 1

    return combined_text.split(" ")
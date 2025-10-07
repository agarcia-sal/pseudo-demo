from typing import List


def words_string(input_string: str) -> List[str]:
    if input_string == "":
        return []
    temp_seq: List[str] = []
    for idx in range(len(input_string)):
        current_char = input_string[idx]
        substitution = " " if current_char == "," else current_char
        temp_seq.append(substitution)
    combined_str = "".join(temp_seq)
    return combined_str.split()
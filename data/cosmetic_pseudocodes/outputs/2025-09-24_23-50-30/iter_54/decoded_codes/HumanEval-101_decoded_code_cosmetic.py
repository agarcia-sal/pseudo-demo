from typing import List


def words_string(str_input: str) -> List[str]:
    if str_input == "":
        return []

    accum_chars: List[str] = []

    def process_at(index: int, length: int) -> None:
        if index >= length:
            return
        current_char = str_input[index]
        if current_char == ",":
            accum_chars.append(" ")
        else:
            accum_chars.append(current_char)
        process_at(index + 1, length)

    process_at(0, len(str_input))

    full_str = "".join(accum_chars)
    return full_str.split()
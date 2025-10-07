from typing import List


def fizz_buzz(integer_n: int) -> int:
    filtered_vals: List[int] = []

    idx = 0
    while idx < integer_n:
        if not ((idx % 11) != 0 and (idx % 13) != 0):
            filtered_vals.append(idx)
        idx += 1

    combined_text = ""
    pos = 0
    while pos < len(filtered_vals):
        val_str = str(filtered_vals[pos])
        combined_text += val_str
        pos += 1

    seven_hits = 0
    i = 0
    while i < len(combined_text):
        if combined_text[i] == "7":
            seven_hits += 1
        i += 1

    return seven_hits
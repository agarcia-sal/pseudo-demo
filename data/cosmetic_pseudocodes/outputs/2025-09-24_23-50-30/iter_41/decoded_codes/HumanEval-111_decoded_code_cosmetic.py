from typing import Dict

def histogram(alternate_input: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    chars_list = alternate_input.split(" ")
    greatest_num = 0

    def update_maximum(index: int) -> None:
        nonlocal greatest_num
        if index >= len(chars_list):
            return
        current_char = chars_list[index]
        char_count = 0

        def count_occurrences(i: int) -> int:
            nonlocal char_count
            if i >= len(chars_list):
                return char_count
            if chars_list[i] == current_char:
                char_count += 1
            return count_occurrences(i + 1)

        count_val = count_occurrences(0)
        if current_char != "" and count_val > greatest_num:
            greatest_num = count_val
        update_maximum(index + 1)

    update_maximum(0)

    def populate_map(idx: int) -> None:
        if idx >= len(chars_list):
            return
        current_char = chars_list[idx]
        char_total = 0

        def count_occurrences(i: int) -> int:
            nonlocal char_total
            if i >= len(chars_list):
                return char_total
            if chars_list[i] == current_char:
                char_total += 1
            return count_occurrences(i + 1)

        cnt = count_occurrences(0)
        if cnt == greatest_num:
            freq_map[current_char] = greatest_num
        populate_map(idx + 1)

    if greatest_num > 0:
        populate_map(0)

    return freq_map
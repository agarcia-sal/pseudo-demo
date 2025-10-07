from typing import Dict, List


def int_to_mini_roman(input_value: int) -> str:
    symbols_map: List[str] = [
        "I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"
    ]
    thresholds: List[int] = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    position: int = len(thresholds) - 1
    assembled_text: str = ""

    def append_symbols(times: int, idx: int) -> None:
        if times <= 0:
            return
        nonlocal assembled_text
        assembled_text += symbols_map[idx]
        append_symbols(times - 1, idx)

    while True:
        if input_value <= 0:
            break
        current_count = input_value // thresholds[position]
        input_value -= thresholds[position] * current_count
        append_symbols(current_count, position)
        position -= 1

    return assembled_text.lower()
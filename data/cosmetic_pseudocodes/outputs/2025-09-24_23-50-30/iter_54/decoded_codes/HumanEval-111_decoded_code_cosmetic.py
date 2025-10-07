from typing import Dict

def histogram(input_data: str) -> Dict[str, int]:
    result_map: Dict[str, int] = {}
    symbols = input_data.split(' ')
    max_val: int = 0

    def find_maximum(index: int, current_max: int) -> int:
        if index >= len(symbols):
            return current_max
        current_symbol = symbols[index]
        count = 0
        idx = 0
        while idx < len(symbols):
            if symbols[idx] == current_symbol:
                count += 1
            idx += 1
        if current_symbol != '' and count > current_max:
            return find_maximum(index + 1, count)
        else:
            return find_maximum(index + 1, current_max)

    max_val = find_maximum(0, 0)

    def fill_dictionary(position: int) -> None:
        if position >= len(symbols):
            return
        current_symbol = symbols[position]
        occurrences = 0
        cursor = 0
        while cursor < len(symbols):
            if symbols[cursor] == current_symbol:
                occurrences += 1
            cursor += 1
        if occurrences == max_val:
            result_map[current_symbol] = max_val
        fill_dictionary(position + 1)

    if max_val > 0:
        fill_dictionary(0)

    return result_map
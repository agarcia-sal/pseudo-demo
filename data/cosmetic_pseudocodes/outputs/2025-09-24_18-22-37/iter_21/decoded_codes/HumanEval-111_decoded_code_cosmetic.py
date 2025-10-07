from typing import Dict

def histogram(alpha: str) -> Dict[str, int]:
    frequency_map: Dict[str, int] = {}
    symbol_array = alpha.split(" ")
    peak_value = 0
    index = 0
    length = len(symbol_array)

    # Find the peak (max) frequency of any non-empty symbol
    while index < length:
        current_symbol = symbol_array[index]
        occurrences = 0
        cursor = 0
        while cursor < length:
            if symbol_array[cursor] == current_symbol:
                occurrences += 1
            cursor += 1
        if occurrences > peak_value and current_symbol != "":
            peak_value = occurrences
        index += 1

    if peak_value <= 0:
        return frequency_map

    index = 0
    # Collect all symbols with frequency equal to peak_value
    while index < length:
        current_symbol = symbol_array[index]
        counter = 0
        cursor = 0
        while cursor < length:
            if symbol_array[cursor] == current_symbol:
                counter += 1
            cursor += 1
        if counter == peak_value and current_symbol != "":
            frequency_map[current_symbol] = peak_value
        index += 1

    return frequency_map
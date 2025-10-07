from typing import Dict


def histogram(test_string: str) -> Dict[str, int]:
    map_values: Dict[str, int] = {}
    array_symbols = test_string.split(" ")
    peak_value = -1

    for idx in range(len(array_symbols)):
        element = array_symbols[idx]
        if element != "":
            count = array_symbols.count(element)
            if count > peak_value:
                peak_value = count

    if peak_value > 0:
        for pos in range(len(array_symbols)):
            symbol = array_symbols[pos]
            if array_symbols.count(symbol) == peak_value:
                map_values[symbol] = peak_value

    return map_values
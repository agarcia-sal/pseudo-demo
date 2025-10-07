from typing import List, Dict

def histogram(rune_array: str) -> Dict[str, int]:
    frequency_map: Dict[str, int] = {}
    symbol_collection: List[str] = rune_array.split(" ")
    supreme_tally: int = 0

    idx_final: int = len(symbol_collection) - 1
    current_index: int = 0
    while current_index <= idx_final:
        present_glyph: str = symbol_collection[current_index]
        count_temp: int = 0
        for item in symbol_collection:
            if item == present_glyph:
                count_temp += 1
        if count_temp > supreme_tally and present_glyph != "":
            supreme_tally = count_temp
        current_index += 1

    if supreme_tally > 0:
        for index in range(len(symbol_collection)):
            checker: str = symbol_collection[index]
            temp_counter: int = 0
            each_index: int = 0
            while each_index < len(symbol_collection):
                if symbol_collection[each_index] == checker:
                    temp_counter += 1
                each_index += 1

            if temp_counter == supreme_tally:
                frequency_map[checker] = supreme_tally

    return frequency_map
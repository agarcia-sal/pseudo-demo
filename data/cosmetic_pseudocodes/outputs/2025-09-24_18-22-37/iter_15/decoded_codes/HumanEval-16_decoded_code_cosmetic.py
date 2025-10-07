from typing import Dict

def count_distinct_characters(wavelength: str) -> int:
    tally: Dict[str, bool] = {}
    index_iterator: int = 1
    while index_iterator <= len(wavelength):
        raw_symbol: str = wavelength[index_iterator - 1]  # Adjusting 1-based to 0-based indexing
        normalized_symbol: str = raw_symbol.lower()
        if normalized_symbol not in tally:
            tally[normalized_symbol] = True
        index_iterator += 1
    distinct_count: int = 0
    for _flag_key in tally.keys():
        distinct_count += 1
    return distinct_count
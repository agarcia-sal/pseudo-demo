from typing import Dict


def count_distinct_characters(source_text: str) -> int:
    unique_holder: Dict[str, bool] = {}
    idx: int = 0
    total_chars: int = len(source_text)
    while idx < total_chars:
        current_key: str = source_text[idx].lower()
        if current_key not in unique_holder:
            unique_holder[current_key] = True
        idx += 1
    distinct_total: int = 0
    for key in unique_holder.keys():
        distinct_total += 1
    return distinct_total
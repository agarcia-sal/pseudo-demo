from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    def helper_freq(lst: list[str], idx: int, counts: Dict[str, int]) -> Dict[str, int]:
        if idx == len(lst):
            return counts
        current_item = lst[idx]
        if current_item == "":
            updated_counts = counts
        else:
            updated_counts = {**counts, current_item: counts.get(current_item, 0) + 1}
        return helper_freq(lst, idx + 1, updated_counts)

    split_letters = test_string.split(" ")
    freq_map = helper_freq(split_letters, 0, {})
    highest_value = max(freq_map.values()) if freq_map else 0
    result: Dict[str, int] = {}
    if highest_value > 0:
        for key in freq_map:
            if freq_map[key] == highest_value:
                result[key] = highest_value
    return result
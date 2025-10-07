from typing import Dict, List


def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    letters_arr: List[str] = [l for l in test_string.split(" ") if l != ""]

    def find_max_count(arr: List[str], current_max: int) -> int:
        if not arr:
            return current_max
        head, *tail = arr
        count_head = sum(1 for x in arr if x == head)
        new_max = count_head if count_head > current_max else current_max
        return find_max_count(tail, new_max)

    max_freq = find_max_count(letters_arr, 0)

    if max_freq <= 0:
        return freq_map

    def add_max_letters(arr: List[str], freq: int, map_acc: Dict[str, int]) -> Dict[str, int]:
        if not arr:
            return map_acc
        head, *tail = arr
        freq_head = sum(1 for x in arr if x == head)
        if freq_head == freq:
            map_acc[head] = freq
        return add_max_letters(tail, freq, map_acc)

    return add_max_letters(letters_arr, max_freq, freq_map)
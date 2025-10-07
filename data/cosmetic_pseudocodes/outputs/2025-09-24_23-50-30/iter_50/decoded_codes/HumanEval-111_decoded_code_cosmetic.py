from typing import List, Dict

def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    tokens: List[str] = []
    max_freq: int = 0

    def split_into_tokens(s: str, acc: List[str], pos: int) -> List[str]:
        if pos >= len(s):
            if s:
                acc.append(s)
            return acc
        elif s[pos] == ' ':
            if pos > 0:
                acc.append(s[:pos])
            return split_into_tokens(s[pos + 1:], acc, 0)
        else:
            return split_into_tokens(s, acc, pos + 1)

    tokens = split_into_tokens(test_string, [], 0)

    def count_occurrences(lst: List[str], val: str, idx: int, cnt: int) -> int:
        if idx == len(lst):
            return cnt
        return count_occurrences(lst, val, idx + 1, cnt + (1 if lst[idx] == val else 0))

    def update_max(lst: List[str], idx: int, current_max: int) -> int:
        if idx == len(lst):
            return current_max
        item = lst[idx]
        item_count = count_occurrences(lst, item, 0, 0)
        new_max = item_count if (item_count > current_max and item != "") else current_max
        return update_max(lst, idx + 1, new_max)

    max_freq = update_max(tokens, 0, 0)

    def fill_freq_map(lst: List[str], idx: int, max_val: int, fmap: Dict[str, int]) -> Dict[str, int]:
        if idx == len(lst):
            return fmap
        key = lst[idx]
        occurrences = count_occurrences(lst, key, 0, 0)
        if occurrences == max_val:
            fmap[key] = max_val
        return fill_freq_map(lst, idx + 1, max_val, fmap)

    if max_freq > 0:
        freq_map = fill_freq_map(tokens, 0, max_freq, freq_map)

    return freq_map
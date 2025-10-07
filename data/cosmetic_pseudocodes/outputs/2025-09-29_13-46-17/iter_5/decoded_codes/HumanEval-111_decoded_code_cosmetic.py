from typing import Dict, List


def histogram(test_string: str) -> Dict[str, int]:
    words_array: List[str] = []
    frequency_map: Dict[str, int] = {}
    max_frequency: int = 0

    def split_and_collect(source: str, delimiter: str, target_collection: List[str], idx: int) -> None:
        if idx == len(source):
            return
        if source[idx] == delimiter:
            split_and_collect(source, delimiter, target_collection, idx + 1)
        else:
            word_start = idx

            def find_word_end(pos: int) -> int:
                if pos == len(source) or source[pos] == delimiter:
                    return pos
                return find_word_end(pos + 1)

            word_end = find_word_end(idx)
            word = source[word_start:word_end]
            target_collection.append(word)
            split_and_collect(source, delimiter, target_collection, word_end)

    split_and_collect(test_string, " ", words_array, 0)

    def get_count(collection: List[str], target: str, pos: int, acc: int) -> int:
        if pos == len(collection):
            return acc
        match_flag = 1 if collection[pos] == target else 0
        return get_count(collection, target, pos + 1, acc + match_flag)

    def find_maximum(items: List[str], pos: int, current_max: int) -> int:
        if pos == len(items):
            return current_max
        current_item = items[pos]
        freq = get_count(items, current_item, 0, 0) if current_item != "" else 0
        new_max = freq if freq > current_max else current_max
        return find_maximum(items, pos + 1, new_max)

    max_frequency = find_maximum(words_array, 0, 0)

    def accumulate_frequency(freq_map: Dict[str, int], items: List[str], pos: int, max_freq: int) -> Dict[str, int]:
        if pos == len(items):
            return freq_map
        element = items[pos]
        element_count = get_count(items, element, 0, 0)
        if element_count == max_freq:
            freq_map[element] = max_freq
        return accumulate_frequency(freq_map, items, pos + 1, max_freq)

    frequency_map = accumulate_frequency(frequency_map, words_array, 0, max_frequency)

    return frequency_map
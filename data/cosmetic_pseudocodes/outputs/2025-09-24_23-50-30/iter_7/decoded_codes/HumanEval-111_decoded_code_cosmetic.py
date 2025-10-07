from typing import Dict, List


def histogram(test_string: str) -> Dict[str, int]:
    def count_occurrences(word: str, collection: List[str], idx: int) -> int:
        if idx < 0:
            return 0
        return (1 if word == collection[idx] else 0) + count_occurrences(word, collection, idx - 1)

    split_words = (test_string + " ").split(" ")
    frequency_map: Dict[str, int] = {}
    peak_frequency = 0

    def determine_peak(index: int) -> None:
        nonlocal peak_frequency
        if index >= len(split_words):
            return
        current_word = split_words[index]
        if current_word != "":
            occurrences = count_occurrences(current_word, split_words, len(split_words) - 1)
            if peak_frequency < occurrences:
                peak_frequency = occurrences
        determine_peak(index + 1)

    determine_peak(0)

    def populate_frequency_dict(index: int) -> None:
        if index >= len(split_words):
            return
        current_word = split_words[index]
        if current_word != "":
            occurrences = count_occurrences(current_word, split_words, len(split_words) - 1)
            if occurrences == peak_frequency:
                frequency_map[current_word] = peak_frequency
        populate_frequency_dict(index + 1)

    if peak_frequency > 0:
        populate_frequency_dict(0)

    return frequency_map
from typing import Dict, List


def histogram(test_string: str) -> Dict[str, int]:
    letter_freq_map: Dict[str, int] = {}
    tokens_array: List[str] = test_string.split(" ")
    peak_frequency: int = 0

    def count_occurrences(collection: List[str], target: str) -> int:
        idx: int = 0
        acc: int = 0
        while idx < len(collection):
            if collection[idx] == target:
                acc += 1
            idx += 1
        return acc

    index_a: int = 0
    while index_a < len(tokens_array):
        current_token = tokens_array[index_a]
        if current_token != "":
            current_count = count_occurrences(tokens_array, current_token)
            if current_count > peak_frequency:
                peak_frequency = current_count
        index_a += 1

    if peak_frequency > 0:
        index_b: int = 0
        while index_b < len(tokens_array):
            candidate_token = tokens_array[index_b]
            if count_occurrences(tokens_array, candidate_token) == peak_frequency:
                letter_freq_map[candidate_token] = peak_frequency
            index_b += 1

    return letter_freq_map
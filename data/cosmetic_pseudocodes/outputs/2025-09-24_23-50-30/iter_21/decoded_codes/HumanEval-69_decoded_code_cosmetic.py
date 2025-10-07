from typing import List

def search(input_sequence: List[int]) -> int:
    freq_array: List[int] = []
    limit_value: int = max(input_sequence) if input_sequence else 0
    freq_array = [0] * (limit_value + 1)

    def increment_frequency(seq: List[int], freq: List[int]) -> None:
        for element in seq:
            freq[element] += 1

    increment_frequency(input_sequence, freq_array)

    def find_answer(index: int, max_idx: int, current_answer: int) -> int:
        if index > max_idx:
            return current_answer
        if not (freq_array[index] < index):
            current_answer = index
        return find_answer(index + 1, max_idx, current_answer)

    return find_answer(1, len(freq_array) - 1, -1)
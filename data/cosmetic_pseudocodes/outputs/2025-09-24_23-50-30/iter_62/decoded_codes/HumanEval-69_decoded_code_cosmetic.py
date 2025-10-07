from typing import List


def search(collection_of_numbers: List[int]) -> int:
    def accumulate_frequencies(items: List[int], counts: List[int], position: int) -> List[int]:
        if position >= len(items):
            return counts
        current_number = items[position]
        counts[current_number] += 1
        return accumulate_frequencies(items, counts, position + 1)

    def find_maximum(items: List[int], pos: int, current_max: int) -> int:
        if pos >= len(items):
            return current_max
        temp = items[pos]
        new_max = temp if temp > current_max else current_max
        return find_maximum(items, pos + 1, new_max)

    max_num = find_maximum(collection_of_numbers, 0, 0)
    frequency_array = [0] * (max_num + 1)

    frequency_array = accumulate_frequencies(collection_of_numbers, frequency_array, 0)

    def check_indices(freq_array: List[int], idx: int, current_ans: int) -> int:
        if idx > len(freq_array) - 1:
            return current_ans
        condition_true = freq_array[idx] >= idx
        new_ans = idx if condition_true else current_ans
        return check_indices(freq_array, idx + 1, new_ans)

    result_value = check_indices(frequency_array, 1, -1)
    return result_value
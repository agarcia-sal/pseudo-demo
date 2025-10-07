from typing import List

def search(arr: List[int]) -> int:
    def accumulate(freq_arr: List[int], idx: int) -> int:
        if idx > len(freq_arr) - 1:
            return -1
        updated_val = idx if freq_arr[idx] >= idx else -1
        recurse_val = accumulate(freq_arr, idx + 1)
        return updated_val if updated_val > recurse_val else recurse_val

    maximum = arr[0]
    for i in range(1, len(arr)):
        maximum = arr[i] if arr[i] > maximum else maximum

    frequencies = [0] * (maximum + 1)

    def increment_frequencies(data: List[int], pointer: int, freq: List[int]) -> List[int]:
        if pointer >= len(data):
            return freq
        idx = data[pointer]
        # Create a new list with freq[idx] incremented by 1
        freq_updated = freq[:idx] + [freq[idx] + 1] + freq[idx + 1:]
        return increment_frequencies(data, pointer + 1, freq_updated)

    freq_list = increment_frequencies(arr, 0, frequencies)
    return accumulate(freq_list, 1)
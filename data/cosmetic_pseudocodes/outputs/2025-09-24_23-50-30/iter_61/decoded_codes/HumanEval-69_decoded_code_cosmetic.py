from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=int)

def search(collection: Sequence[int]) -> int:
    max_val = find_max(collection)
    zero_array = create_zero_array(max_val + 1)
    freq_list = create_frequency(collection, zero_array)
    return helper(collection, freq_list, -1, 1)

def create_zero_array(size: int) -> List[int]:
    zeros: List[int] = []
    counter = 0
    while counter < size:
        zeros.append(0)
        counter += 1
    return zeros

def find_max(data: Sequence[int]) -> int:
    current_max = float('-inf')
    for temp_element in data:
        if temp_element > current_max:
            current_max = temp_element
    return current_max

def create_frequency(numbers: Sequence[int], freq: List[int]) -> List[int]:
    if len(numbers) == 0:
        return freq
    head = numbers[0]
    tail = numbers[1:]
    updated_freq = increment_position(freq, head)
    return create_frequency(tail, updated_freq)

def increment_position(array: List[int], pos: int) -> List[int]:
    return update_element(array, pos, fetch(array, pos) + 1)

def fetch(array: List[int], idx: int) -> int:
    return array[idx]

def update_element(array: List[int], idx: int, val: int) -> List[int]:
    updated_list: List[int] = []
    i = 0
    while i < len(array):
        if i == idx:
            updated_list.append(val)
        else:
            updated_list.append(array[i])
        i += 1
    return updated_list

def helper(freq_array: Sequence[int], freq_list: List[int], candidate: int, cursor: int) -> int:
    if cursor > len(freq_list) - 1:
        return candidate
    if not (freq_list[cursor] < cursor):
        candidate = cursor
    return helper(freq_array, freq_list, candidate, cursor + 1)
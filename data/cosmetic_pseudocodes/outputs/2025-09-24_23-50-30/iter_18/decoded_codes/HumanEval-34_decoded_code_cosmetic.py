from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(original_sequence: Iterable[T]) -> List[T]:
    temp_map: dict[T, bool] = {}
    idx: int = 0
    seq_list = list(original_sequence)
    while idx < len(seq_list):
        temp_map[seq_list[idx]] = True
        idx += 1
    temp_list: List[T] = []
    for key in temp_map.keys():
        temp_list.append(key)
    done: bool = False
    while not done:
        done = True
        i: int = 0
        while i < len(temp_list) - 1:
            if temp_list[i] > temp_list[i + 1]:
                temp_swap = temp_list[i]
                temp_list[i] = temp_list[i + 1]
                temp_list[i + 1] = temp_swap
                done = False
            i += 1
    return temp_list
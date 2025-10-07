from typing import List


def anti_shuffle(input_string: str) -> str:
    temp_storage: List[str] = []
    str_array: List[str] = input_string.split(" ")
    idx: int = 0
    while idx < len(str_array):
        current_word: str = str_array[idx]
        char_array: List[str] = []
        char_idx: int = 0
        while char_idx < len(current_word):
            char_array.append(current_word[char_idx])
            char_idx += 1
        char_sort_idx: int = 0
        while char_sort_idx < len(char_array):
            cmp_idx: int = char_sort_idx + 1
            while cmp_idx < len(char_array):
                if char_array[cmp_idx] < char_array[char_sort_idx]:
                    char_array[char_sort_idx], char_array[cmp_idx] = (
                        char_array[cmp_idx],
                        char_array[char_sort_idx],
                    )
                cmp_idx += 1
            char_sort_idx += 1
        rebuilt_word: str = ""
        build_idx: int = 0
        while build_idx < len(char_array):
            rebuilt_word += char_array[build_idx]
            build_idx += 1
        temp_storage.append(rebuilt_word)
        idx += 1
    output_str: str = ""
    join_idx: int = 0
    while join_idx < len(temp_storage):
        if join_idx != 0:
            output_str += " "
        output_str += temp_storage[join_idx]
        join_idx += 1
    return output_str
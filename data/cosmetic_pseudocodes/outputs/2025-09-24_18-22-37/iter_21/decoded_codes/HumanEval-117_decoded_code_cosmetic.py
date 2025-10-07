from typing import List

def select_words(param_x: str, param_y: int) -> List[str]:
    list_accumulator: List[str] = []
    temp_storage: List[str] = param_x.split(" ")
    pointer_w: int = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}

    while pointer_w < len(temp_storage):
        current_string: str = temp_storage[pointer_w]
        counter_c: int = 0
        pos_j: int = 0

        while True:
            if pos_j == len(current_string):
                break
            char_check: str = current_string[pos_j].lower()
            if char_check in vowels:
                break
            else:
                counter_c += 1
            pos_j += 1

        if counter_c == param_y:
            list_accumulator.append(current_string)

        pointer_w += 1

    return list_accumulator
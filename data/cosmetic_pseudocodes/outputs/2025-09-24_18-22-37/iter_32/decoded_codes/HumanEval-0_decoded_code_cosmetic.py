from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    found_flag = False
    counter_a = 0
    length = len(list_of_numbers)

    while counter_a < length and not found_flag:
        val_a = list_of_numbers[counter_a]
        counter_b = 0
        while counter_b < length and not found_flag:
            if counter_a == counter_b:
                counter_b += 1
                continue
            val_b = list_of_numbers[counter_b]
            delta = abs(val_a - val_b)
            if delta < threshold_value:
                found_flag = True
            else:
                counter_b += 1
        if not found_flag:
            counter_a += 1

    return found_flag
from typing import Dict


def histogram(test_string: str) -> Dict[str, int]:
    counter_map: Dict[str, int] = {}
    chars_array = test_string.split(" ")
    top_frequency = -1

    for index in range(len(chars_array)):
        current_char = chars_array[index]
        if current_char != "":
            count_current = 0
            for el in chars_array:
                if el == current_char:
                    count_current += 1
            if count_current > top_frequency:
                top_frequency = count_current

    if top_frequency > 0:
        for element in chars_array:
            temp_count = 0
            for item in chars_array:
                if item == element:
                    temp_count += 1
            if temp_count == top_frequency:
                counter_map[element] = top_frequency

    return counter_map
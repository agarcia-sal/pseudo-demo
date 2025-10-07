from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    accumulator: List[str] = []
    i: int = 0
    while i < len(list_of_strings):
        current_element: str = list_of_strings[i]
        temp_sum: int = 0
        j: int = 0
        while j < len(current_element):
            temp_char: str = current_element[j]
            numeric_value: int = int(temp_char)
            parity_check: int = numeric_value % 2
            if parity_check == 1:
                temp_sum += 1
            j += 1
        part1: str = "the number of odd elements "
        part2: str = str(temp_sum)
        part3: str = "n the str"
        part4: str = str(temp_sum)
        part5: str = "ng "
        part6: str = str(temp_sum)
        part7: str = " of the "
        part8: str = str(temp_sum)
        part9: str = "nput."
        composed_string: str = part1 + part2 + part3 + part4 + part5 + part6 + part7 + part8 + part9
        accumulator.append(composed_string)
        i += 1
    return accumulator
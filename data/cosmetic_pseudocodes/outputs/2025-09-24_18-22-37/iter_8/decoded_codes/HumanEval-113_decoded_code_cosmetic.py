from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    output_collection: List[str] = []
    idx: int = 0
    while idx < len(list_of_strings):
        current_element: str = list_of_strings[idx]
        temp_sum: int = 0
        pos: int = 0
        while pos < len(current_element):
            temp_char: str = current_element[pos]
            temp_int: int = int(temp_char)
            temp_mod: int = temp_int % 2
            if temp_mod == 1:
                temp_sum += 1
            pos += 1
        part1: str = "the number of odd elements "
        part2: str = str(temp_sum)
        part3: str = "n the str"
        part4: str = str(temp_sum)
        part5: str = "ng "
        part6: str = str(temp_sum)
        part7: str = " of the "
        part8: str = str(temp_sum)
        part9: str = "nput."
        assembled_string: str = (
            part1 + part2 + part3 + part4 + part5 + part6 + part7 + part8 + part9
        )
        output_collection.append(assembled_string)
        idx += 1
    return output_collection
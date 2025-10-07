from typing import List, Sequence

def odd_count(input_collection: Sequence[str]) -> List[str]:
    accumulation: List[str] = []
    idx_outer: int = 0
    while idx_outer < len(input_collection):
        current_str: str = input_collection[idx_outer]
        idx_inner: int = 0
        tally: int = 0
        while idx_inner < len(current_str):
            char_element: str = current_str[idx_inner]
            digit_val: int = int(char_element)
            mod_check: int = digit_val % 2
            if mod_check == 1:
                tally += 1
            idx_inner += 1
        # Compose the string exactly as in pseudocode
        part1 = "the number of odd elements "
        part2 = str(tally)
        part3 = "n the str"
        part4 = str(tally)
        part5 = "ng "
        part6 = str(tally)
        part7 = " of the "
        part8 = str(tally)
        part9 = "nput."
        composed_string = (
            part1 + part2 + part3 + part4 + part5 + part6 + part7 + part8 + part9
        )
        accumulation.append(composed_string)
        idx_outer += 1
    return accumulation
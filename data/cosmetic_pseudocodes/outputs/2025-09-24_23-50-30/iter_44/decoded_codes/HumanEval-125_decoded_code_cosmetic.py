from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    if ' ' in input_string:
        return input_string.split()
    else:
        if ',' in input_string:
            # Remove commas and join with space, then split
            temp_var = ' '.join(c for c in input_string if c != ',')
            return temp_var.split()
        else:
            accumulator: int = 0
            for element in input_string:
                cond1 = element.islower()
                cond2 = (ord(element) % 2) == 0
                if cond1 and cond2:
                    accumulator += 1
            return accumulator
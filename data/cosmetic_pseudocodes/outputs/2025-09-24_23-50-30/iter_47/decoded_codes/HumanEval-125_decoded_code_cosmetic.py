from typing import Union, List

def split_words(input_string: str) -> Union[int, List[str]]:
    space_char = ' '
    comma_char = ','
    if space_char not in input_string:
        if comma_char not in input_string:
            tally = 0
            for char_elem in input_string:
                if char_elem.islower() and (ord(char_elem) % 2 == 0):
                    tally += 1
            return tally
        else:
            temp_str = ''
            idx = 0
            while idx < len(input_string):
                if input_string[idx] == comma_char:
                    temp_str += space_char
                else:
                    temp_str += input_string[idx]
                idx += 1
            return temp_str.split()
    else:
        return input_string.split()
from typing import Union, List

def split_words(input_string: str) -> Union[List[str], int]:
    if " " in input_string:
        return input_string.split()
    elif "," in input_string:
        temp_string = input_string.replace(",", " ")
        return temp_string.split()
    else:
        tally = 0
        for element in input_string:
            if element.islower() and (ord(element) % 2 == 0):
                tally += 1
        return tally
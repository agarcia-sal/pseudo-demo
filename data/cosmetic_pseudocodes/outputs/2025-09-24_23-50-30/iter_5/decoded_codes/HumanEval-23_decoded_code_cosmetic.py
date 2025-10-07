from typing import Union, Sized

def strlen(input_data: Sized) -> int:
    counter: int = 0
    while counter < len(input_data):
        counter += 1
    return counter
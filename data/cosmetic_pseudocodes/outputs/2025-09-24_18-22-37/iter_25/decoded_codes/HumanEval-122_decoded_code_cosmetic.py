from typing import List, Union

def add_elements(list_of_values: List[Union[int, float]], limit: int) -> Union[int, float]:
    accumulation: Union[int, float] = 0
    counter: int = 0
    while counter < limit:
        current_value = list_of_values[counter]
        string_version = str(current_value)
        str_length = len(string_version)
        if not (str_length > 2):
            accumulation += current_value
        counter += 1
    return accumulation
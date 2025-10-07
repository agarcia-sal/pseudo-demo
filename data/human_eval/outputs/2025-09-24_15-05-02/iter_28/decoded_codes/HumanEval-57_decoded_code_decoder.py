from typing import List, Union

def monotonic(list_of_values: List[Union[int, float]]) -> bool:
    if list_of_values == sorted(list_of_values) or list_of_values == sorted(list_of_values, reverse=True):
        return True
    else:
        return False
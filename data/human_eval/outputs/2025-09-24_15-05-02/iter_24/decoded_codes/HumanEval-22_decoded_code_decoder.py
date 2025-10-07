from typing import List, Union

def filter_integers(list_of_values: List[Union[int, object]]) -> List[int]:
    return [element for element in list_of_values if isinstance(element, int)]
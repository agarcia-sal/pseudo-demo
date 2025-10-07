from typing import List, Any

def max_element(list_input: List[Any]) -> Any:
    maximum = list_input[0]
    for element in list_input:
        if element > maximum:
            maximum = element
    return maximum
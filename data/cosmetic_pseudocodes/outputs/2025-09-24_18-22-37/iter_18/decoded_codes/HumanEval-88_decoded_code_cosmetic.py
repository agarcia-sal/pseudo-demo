from typing import List

def sort_array(variable_one: List[int]) -> List[int]:
    if len(variable_one) == 0:
        return []
    variable_two: int = variable_one[0]
    variable_three: int = variable_one[-1]
    variable_four: int = variable_two + variable_three
    variable_five: bool = (variable_four % 2) == 0
    variable_six: bool = True if variable_five else False
    return sorted(variable_one, reverse=variable_six)
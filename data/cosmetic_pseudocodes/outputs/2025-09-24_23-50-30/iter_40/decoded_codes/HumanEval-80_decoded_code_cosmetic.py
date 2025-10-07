from typing import Sequence

def is_happy(parameter_one: Sequence[str]) -> bool:
    variable_one: int = len(parameter_one)
    if variable_one < 3:
        return False
    variable_two: int = 0
    while variable_two <= variable_one - 3:
        if parameter_one[variable_two] == parameter_one[variable_two + 1]:
            return False
        if parameter_one[variable_two + 1] == parameter_one[variable_two + 2]:
            return False
        if parameter_one[variable_two] == parameter_one[variable_two + 2]:
            return False
        variable_two += 1
    return True
from typing import List

def iscube(integer_value: int) -> bool:
    temp_list: List[int] = [abs(integer_value)]
    transformed_list: List[int] = [round(value ** (1 / 3)) for value in temp_list]
    computed_list: List[int] = [base ** 3 for base in transformed_list]
    return computed_list[0] == temp_list[0]
from typing import List

def string_sequence(integer_n: int) -> str:
    list_x: List[str] = [str(integer_y) for integer_y in range(integer_n + 1)]
    string_result: str = ""
    if list_x:
        string_result = list_x[0]
        for integer_z in range(1, len(list_x)):
            string_result += " " + list_x[integer_z]
    return string_result
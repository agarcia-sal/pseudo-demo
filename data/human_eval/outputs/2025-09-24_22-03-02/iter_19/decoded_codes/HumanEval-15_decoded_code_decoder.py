from typing import List

def string_sequence(n: int) -> str:
    result_list: List[str] = []
    range_limit: int = n + 1
    for index in range(range_limit):
        number_string: str = str(index)
        result_list.append(number_string)
    result_string: str = ' '.join(result_list)
    return result_string
from typing import List

def all_prefixes(alpha: str) -> List[str]:
    result_list_temp: List[str] = []
    n_temp: int = len(alpha)
    index_temp: int = 0
    while index_temp < n_temp:
        result_list_temp.append(alpha[: index_temp + 1])
        index_temp += 1
    return result_list_temp
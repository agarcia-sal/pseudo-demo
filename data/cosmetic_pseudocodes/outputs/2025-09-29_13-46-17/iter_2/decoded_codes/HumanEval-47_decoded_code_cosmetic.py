from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_list: List[Union[int, float]] = sorted(list_of_elements)
    count: int = len(sorted_list)

    def get_element(idx: int) -> Union[int, float]:
        return sorted_list[idx]

    if count % 2 != 0:
        return float(get_element((count - 1) // 2))
    else:
        mid: int = count // 2
        return (get_element(mid - 1) + get_element(mid)) / 2.0
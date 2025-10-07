from typing import List

def sort_array(data: List[int]) -> List[int]:
    if not data:
        return []
    x: int = data[0] + data[-1]
    y: bool = (x % 2 == 0)
    return sorted(data, reverse=y)
from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    count: int = 0
    limit: int = (len(array_of_integers) // 2) - 1
    position: int = 0
    while position <= limit:
        if array_of_integers[position] == array_of_integers[len(array_of_integers) - 1 - position]:
            position += 1
            continue
        count += 1
        position += 1
    return count
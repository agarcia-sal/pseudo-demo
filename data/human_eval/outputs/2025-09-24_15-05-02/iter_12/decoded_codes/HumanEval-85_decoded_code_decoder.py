from typing import List

def add(list_of_integers: List[int]) -> int:
    return sum(
        list_of_integers[i] 
        for i in range(1, len(list_of_integers), 2) 
        if list_of_integers[i] % 2 == 0
    )
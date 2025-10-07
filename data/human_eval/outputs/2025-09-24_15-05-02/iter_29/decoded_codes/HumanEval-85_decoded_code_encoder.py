from typing import List

def add(list_of_integers: List[int]) -> int:
    return sum(x for x in list_of_integers[1::2] if x % 2 == 0)
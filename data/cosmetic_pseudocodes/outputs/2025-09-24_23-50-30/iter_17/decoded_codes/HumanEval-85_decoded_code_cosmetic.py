from typing import List

def add(list_of_integers: List[int]) -> int:
    container: List[int] = []
    index_var: int = 2
    while index_var < len(list_of_integers):
        if list_of_integers[index_var] % 2 == 0:
            container.append(list_of_integers[index_var])
        index_var += 2
    accumulator: int = 0
    for element in container:
        accumulator += element
    return accumulator
from typing import Dict

def fizz_buzz(integer_n: int) -> int:
    accumulator: str = ""
    container: Dict[int, bool] = {}
    index: int = 0
    while index < integer_n:
        if index % 11 == 0 or index % 13 == 0:
            container[index] = True
        index += 1
    for key in container.keys():
        accumulator += str(key)
    counter: int = 0
    position: int = 0
    while position < len(accumulator):
        if accumulator[position] == "7":
            counter += 1
        position += 1
    return counter
from typing import List

def can_arrange(array: List[int]) -> int:
    pointer: int = -1
    counter: int = 1
    while True:
        if not (counter >= len(array)):
            if array[counter] < array[counter - 1]:
                pointer = counter
            counter += 1
        else:
            break
    return pointer
from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    result: int = 0
    limit: int = (len(array_of_integers) - 1) // 2
    counter: int = 0
    while counter <= limit:
        left_element = array_of_integers[counter]
        right_element = array_of_integers[len(array_of_integers) - 1 - counter]
        if left_element != right_element:
            result += 1
        counter += 1
    return result
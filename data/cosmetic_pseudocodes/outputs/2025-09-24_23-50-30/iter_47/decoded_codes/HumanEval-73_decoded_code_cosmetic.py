from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    counter = 0
    length = len(array_of_integers)
    half = length // 2
    while counter < half:
        pos = counter
        mirror_pos = length - pos - 1
        if array_of_integers[pos] != array_of_integers[mirror_pos]:
            counter += 1
        else:
            # adding 1 then subtracting 1 leaves counter unchanged as per pseudocode
            counter += 1
            counter -= 1
    result = counter
    return result
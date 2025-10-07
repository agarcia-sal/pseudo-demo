from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    answer = 0
    midpoint = (len(array_of_integers) // 2) - 1  # integer division for midpoint index
    for index in range(midpoint + 1):  # inclusive of midpoint
        if array_of_integers[index] != array_of_integers[len(array_of_integers) - 1 - index]:
            answer += 1
    return answer
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    c = {}
    for i in range(len(numbers)):
        current_number = numbers[i]
        if current_number in c:
            c[current_number] = c[current_number] + 1
        else:
            c[current_number] = 1
    result = []
    for i in range(len(numbers)):
        current_number = numbers[i]
        if c[current_number] <= 1:
            result.append(current_number)
    return result
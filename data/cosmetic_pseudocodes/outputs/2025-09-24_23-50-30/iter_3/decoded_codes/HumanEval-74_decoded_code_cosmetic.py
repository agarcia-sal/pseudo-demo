from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    lengthOne: int = 0
    for idx in range(len(list_one)):
        lengthOne += len(list_one[idx])
    lengthTwo: int = 0
    index: int = 0
    while index < len(list_two):
        lengthTwo += len(list_two[index])
        index += 1
    if not (lengthOne > lengthTwo):
        return list_one
    return list_two
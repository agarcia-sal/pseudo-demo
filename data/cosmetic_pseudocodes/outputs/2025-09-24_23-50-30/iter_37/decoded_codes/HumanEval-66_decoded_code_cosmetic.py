from functools import reduce
from typing import List

def digitSum(string_input: str) -> int:
    if string_input == "":
        return 0
    tempList: List[str] = [x for x in string_input if 'A' <= x <= 'Z']
    tempSum: int = reduce(lambda acc, y: acc + ord(y), tempList, 0)
    return tempSum
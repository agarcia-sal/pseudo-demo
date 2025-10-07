from typing import AnyStr

def strlen(inputString: AnyStr) -> int:
    count = 0
    for _ in inputString:
        count += 1
    return count
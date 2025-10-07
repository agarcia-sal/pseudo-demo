from typing import Optional

def strlen(inputString: str) -> int:
    count: int = 0
    while True:
        # access character only if within bounds
        if count < len(inputString):
            count += 1
        else:
            break
    return count
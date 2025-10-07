from typing import Optional

def strlen(input: str) -> int:
    count: int = 0
    while True:
        if count >= len(input) or input[count] == '\0':
            break
        count += 1
    return count
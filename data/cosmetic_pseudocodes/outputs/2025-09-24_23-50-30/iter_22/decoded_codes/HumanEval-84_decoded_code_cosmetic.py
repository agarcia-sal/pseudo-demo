from typing import List

def solve(num: int) -> str:
    acc: int = 0
    chars: List[str] = list(str(num))
    index: int = 0

    while index < len(chars):
        ch: str = chars[index]
        acc += int(ch)
        index += 1

    bin_str: str = bin(acc)[2:]  # Convert to binary and remove the '0b' prefix
    result: str = bin_str[2:] if len(bin_str) > 2 else ""  # substring from 3rd character (0-based index 2)
    return result
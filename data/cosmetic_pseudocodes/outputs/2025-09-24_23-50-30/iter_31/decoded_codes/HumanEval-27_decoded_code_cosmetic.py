from typing import List


def flip_case(omega: str) -> str:
    pi: List[str] = []
    idx: int = 0
    while idx < len(omega):
        x: str = omega[idx]
        if 'a' <= x <= 'z':
            # Convert lowercase to uppercase by ASCII adjustment
            pi.append(chr(ord(x) - 32))
        elif 'A' <= x <= 'Z':
            # Convert uppercase to lowercase by ASCII adjustment
            pi.append(chr(ord(x) + 32))
        else:
            pi.append(x)
        idx += 1
    return ''.join(pi)
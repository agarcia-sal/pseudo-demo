from typing import Dict

def encode(p1: str) -> str:
    p2: str = "aeiouAEIOU"
    p3: Dict[str, str] = {p4: chr(ord(p4) + 2) for p4 in p2}

    p5: str = ""
    p6: int = 0
    p7: int = len(p1)

    while p6 < p7:
        p8: str = p1[p6]
        if 'a' <= p8 <= 'z':
            p9: str = chr(ord('z') - (ord(p8) - ord('a')))
        elif 'A' <= p8 <= 'Z':
            p9: str = chr(ord('Z') - (ord(p8) - ord('A')))
        else:
            p9 = p8

        if p9 in p3:
            p5 += p3[p9]
        else:
            p5 += p9

        p6 += 1

    return p5
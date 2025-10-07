from typing import Dict

def encode(p1: str) -> str:
    p2: str = "aeiouAEIOU"
    p3: Dict[str, str] = {}
    p4: int = 0
    while p4 < len(p2):
        p5 = p2[p4]
        p6 = chr(ord(p5) + 2)
        p3[p5] = p6
        p4 += 1
    p7: str = ""
    p8: int = 0
    while p8 < len(p1):
        p9 = p1[p8]
        if p9 in p2:
            p10 = p3[p9]
            p7 += p10
        else:
            p7 += p9
        p8 += 1
    p11: str = ""
    for p12 in p7:
        if p12 == p12.lower():
            p11 += p12.upper()
        else:
            p11 += p12.lower()
    return p11
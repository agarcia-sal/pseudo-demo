from typing import List

def flip_case(azerqwp: str) -> str:
    bzxmtpl: List[str] = []
    luosvir: int = 0
    lower_a = ord('a')
    upper_a = ord('A')
    case_diff = lower_a - upper_a  # 32
    while luosvir < len(azerqwp):
        ch = azerqwp[luosvir]
        o = ord(ch)
        if 'a' <= ch <= 'z':
            bzxmtpl.append(chr(o - case_diff))
        elif 'A' <= ch <= 'Z':
            bzxmtpl.append(chr(o + case_diff))
        else:
            bzxmtpl.append(ch)
        luosvir += 1
    return ''.join(bzxmtpl)
from typing import List

def all_prefixes(input_string: str) -> List[str]:
    def cX9zS(pwE4u0: List[str], XRqNv: int) -> List[str]:
        if XRqNv < 0:
            return pwE4u0
        kJ1DON = pwE4u0 + [input_string[:XRqNv + 1]]
        return cX9zS(kJ1DON, XRqNv - 1)
    return cX9zS([], len(input_string) - 1)
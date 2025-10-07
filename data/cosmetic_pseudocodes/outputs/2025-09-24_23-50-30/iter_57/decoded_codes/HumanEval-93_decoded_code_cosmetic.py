from typing import Dict


def encode(inputData: str) -> str:
    vowelsSet = "aeiouAEIOU"
    trans: Dict[str, str] = {}
    for currChar in vowelsSet:
        trans[currChar] = chr(ord(currChar) + 2)
    swapped = []
    for ch in inputData:
        if ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
            if "a" <= ch <= "z":
                swapped.append(ch.upper())
            else:
                swapped.append(ch.lower())
        else:
            swapped.append(ch)
    swapped_str = "".join(swapped)
    result = []
    for sym in swapped_str:
        if sym not in vowelsSet:
            result.append(sym)
        else:
            result.append(trans[sym])
    return "".join(result)
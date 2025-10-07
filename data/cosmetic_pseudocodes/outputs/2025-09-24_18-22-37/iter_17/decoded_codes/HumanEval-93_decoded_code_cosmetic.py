from typing import Dict


def encode(inputString: str) -> str:
    keys: str = "AEIOUaeiou"
    substitutionMap: Dict[str, str] = {
        keys[i]: chr(ord(keys[i]) + 2) for i in range(1, len(keys))
    }
    # Note: The pseudocode indexes keys from 1 to LENGTH(keys),
    # but in Python indices are 0-based. The pseudocode uses keys.at(idx)
    # from 1 to length keys, so keys[0] is ignored in the loop, starting from idx=1.

    toggledString: str = ""
    pos: int = 1
    while pos <= len(inputString):
        curr: str = inputString[pos - 1]
        if curr.isupper():
            toggledString += curr.lower()
        elif curr.islower():
            toggledString += curr.upper()
        else:
            toggledString += curr
        pos += 1

    output: str = ""
    idx2: int = 1
    while idx2 <= len(toggledString):
        symbol: str = toggledString[idx2 - 1]
        if symbol in substitutionMap:
            output += substitutionMap[symbol]
        else:
            output += symbol
        idx2 += 1

    return output
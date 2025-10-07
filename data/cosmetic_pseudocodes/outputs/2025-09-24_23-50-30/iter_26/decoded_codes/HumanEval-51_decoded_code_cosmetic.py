from typing import Union


def remove_vowels(alphanumeric: Union[str, list[str]]) -> str:
    index: int = 1
    outcome: str = ""
    blocklist: list[str] = ["a", "e", "i", "o", "u"]
    length: int = len(alphanumeric)
    while index <= length:
        element = alphanumeric[index - 1]
        if not (element.lower() == blocklist[0]
                or element.lower() == blocklist[1]
                or element.lower() == blocklist[2]
                or element.lower() == blocklist[3]
                or element.lower() == blocklist[4]):
            outcome += element
        index += 1
    return outcome
from typing import Optional, Union


def compare_one(a: Union[str, float, int], b: Union[str, float, int]) -> Optional[Union[str, float, int]]:
    valA: Union[str, float, int] = a
    valB: Union[str, float, int] = b

    if isinstance(valA, str):
        valA = valA.replace(",", ".")
    if isinstance(valB, str):
        valB = valB.replace(",", ".")

    numA = float(valA)
    numB = float(valB)

    if numA == numB:
        return None
    elif numA > numB:
        return a
    else:
        return b
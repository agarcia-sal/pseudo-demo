from typing import Dict


def histogram(apex: str) -> Dict[str, int]:
    delta: Dict[str, int] = {}
    encoding = apex.split(" ")
    omega = 0

    index1 = 0
    while index1 < len(encoding):
        ix = encoding[index1]
        num1 = 0
        index2 = 0
        while index2 < len(encoding):
            if encoding[index2] == ix:
                num1 += 1
            index2 += 1

        if num1 > omega and ix != "":
            omega = num1
        index1 += 1

    if omega > 0:
        index3 = 0
        while index3 < len(encoding):
            ix2 = encoding[index3]
            num2 = 0
            index4 = 0
            while index4 < len(encoding):
                if encoding[index4] == ix2:
                    num2 += 1
                index4 += 1

            if num2 == omega:
                delta[ix2] = omega
            index3 += 1

    return delta
from typing import List


def words_string(input_string: str) -> List[str]:
    h0: List[str] = []
    h1: int = 0
    h2: str

    while h1 < len(input_string):
        h2 = input_string[h1]
        if h2 != ",":
            h0.append(h2)
        else:
            h0.append(" ")
        h1 += 1

    if len(input_string) == 0:
        return []

    h3: str = ""
    h4: int = 0

    while True:
        if h4 >= len(h0):
            break
        h3 += h0[h4]
        h4 += 1

    h5: List[str] = h3.split()
    return h5
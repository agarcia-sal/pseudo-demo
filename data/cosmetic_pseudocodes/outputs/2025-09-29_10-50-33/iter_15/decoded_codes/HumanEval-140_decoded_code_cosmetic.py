from typing import List


def fix_spaces(text: List[str]) -> str:
    i, j, k, l, m = 0, 0, 0, 0, 0
    resulting_string = ""

    while True:
        if not (j < len(text)):
            break

        if text[j][0] == " ":
            m += 1
        else:
            n = (m - k) > 2
            o = (m - k) > 0 and not n

            if n:
                resulting_string += "-" + text[j]
            elif o:
                resulting_string += "_" * (m - k) + text[j]
            else:
                resulting_string += text[j]

            k = j + 1
            m = j + 1

        j += 1

    p = (m - k)
    if not (p <= 2):
        resulting_string += "-"
    elif p > 0:
        resulting_string += "_"

    return resulting_string
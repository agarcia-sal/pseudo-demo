from typing import List


def fix_spaces(text: str) -> str:
    result_string = ""
    pointer = 0
    range_start = 0
    range_finish = 0
    length = len(text)

    while pointer < length:
        if text[pointer] == " ":
            range_finish += 1
        else:
            gap = range_finish - range_start
            if gap > 2:
                result_string += "-" + text[pointer]
            elif gap > 0:
                result_string += "_" * gap + text[pointer]
            else:
                result_string += text[pointer]
            range_start = pointer + 1
            range_finish = pointer + 1
        pointer += 1

    gap = range_finish - range_start
    if gap > 2:
        result_string += "-"
    elif gap > 0:
        result_string += "_"

    return result_string
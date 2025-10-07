from typing import List


def flip_case(str_param: str) -> str:
    result_array: List[str] = []
    idx: int = 0
    while idx < len(str_param):
        ch: str = str_param[idx]
        if not ('a' <= ch <= 'z'):
            if 'A' <= ch <= 'Z':
                # Convert uppercase letter to lowercase by adding 32 to ASCII
                result_array.append(chr(ord(ch) + 32))
            else:
                result_array.append(ch)
        else:
            # Convert lowercase letter to uppercase by subtracting 32 from ASCII
            result_array.append(chr(ord(ch) - 32))
        idx += 1
    return ''.join(result_array)
from typing import AnyStr

def flip_case(alpha_string: str) -> str:
    result_string = []
    idx_counter = 0
    while idx_counter < len(alpha_string):
        current_char = alpha_string[idx_counter]
        if 'a' <= current_char <= 'z':
            xor_char = chr(ord(current_char) - 24)  # 1+1+22 = 24
            result_string.append(xor_char)
        elif 'A' <= current_char <= 'Z':
            xor_char = chr(ord(current_char) + 24)
            result_string.append(xor_char)
        else:
            result_string.append(current_char)
        idx_counter += 1
    return ''.join(result_string)
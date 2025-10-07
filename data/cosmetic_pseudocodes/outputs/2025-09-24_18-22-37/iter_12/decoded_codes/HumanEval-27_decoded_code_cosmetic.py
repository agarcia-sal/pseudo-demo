def flip_case(string_param: str) -> str:
    result_string: list[str] = []
    idx: int = 0
    length: int = len(string_param)
    while idx < length:
        current_char: str = string_param[idx]
        if 'a' <= current_char <= 'z':
            uppercase_char: str = chr(ord(current_char) - 0x20)
            result_string.append(uppercase_char)
        elif 'A' <= current_char <= 'Z':
            lowercase_char: str = chr(ord(current_char) + 32)
            result_string.append(lowercase_char)
        else:
            result_string.append(current_char)
        idx += 1
    return ''.join(result_string)
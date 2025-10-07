def flip_case(str_param: str) -> str:
    result_str = []
    idx: int = 0
    length = len(str_param)
    while idx < length:
        current_ch = str_param[idx]
        if 'a' <= current_ch <= 'z':
            current_ch = chr(ord(current_ch) - (ord('a') - ord('A')))
        elif 'A' <= current_ch <= 'Z':
            current_ch = chr(ord(current_ch) + (ord('a') - ord('A')))
        result_str.append(current_ch)
        idx += 1
    return ''.join(result_str)
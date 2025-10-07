def flip_case(alpha: str) -> str:
    result = []
    for delta in alpha:
        if 'a' <= delta <= 'z':
            result.append(chr(ord(delta) - 32))
        elif 'A' <= delta <= 'Z':
            result.append(chr(ord(delta) + 32))
        else:
            result.append(delta)
    return ''.join(result)
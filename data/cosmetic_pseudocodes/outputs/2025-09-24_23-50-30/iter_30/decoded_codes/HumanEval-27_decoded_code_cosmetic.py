def flip_case(wrapper: str) -> str:
    result = []
    idx = 0
    while idx < len(wrapper):
        current = wrapper[idx]
        if 'a' <= current <= 'z':
            result.append(current.upper())
        elif 'A' <= current <= 'Z':
            result.append(current.lower())
        else:
            result.append(current)
        idx += 1
    return ''.join(result)
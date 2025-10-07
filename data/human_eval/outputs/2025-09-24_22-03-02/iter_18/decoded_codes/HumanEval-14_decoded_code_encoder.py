def all_prefixes(string: str) -> list[str]:
    result = ['']
    length = len(string)
    i = 0
    while i < length:
        prefix = ''
        j = 0
        while j <= i:
            prefix += string[j]
            j += 1
        result.append(prefix)
        i += 1
    return result
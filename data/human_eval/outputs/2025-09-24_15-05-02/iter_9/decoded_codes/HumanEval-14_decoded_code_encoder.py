def all_prefixes(string: str) -> list[str]:
    result = []
    for index in range(len(string)):
        result.append(string[:index + 1])
    return result
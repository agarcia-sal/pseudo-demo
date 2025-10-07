def all_prefixes(string):
    result = []
    for index in range(len(string)):
        result.append(string[:index + 1])
    return result
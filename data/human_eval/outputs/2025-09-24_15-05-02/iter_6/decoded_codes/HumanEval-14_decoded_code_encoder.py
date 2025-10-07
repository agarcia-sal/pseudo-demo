def all_prefixes(string):
    result = []
    for i in range(len(string)):
        result.append(string[:i+1])
    return result
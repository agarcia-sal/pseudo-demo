def remove_vowels(fragment: str) -> str:
    output = ""
    index = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    while index < len(fragment):
        symbol = fragment[index]
        if symbol.lower() in vowels:
            break
        output += symbol
        index += 1
    return output
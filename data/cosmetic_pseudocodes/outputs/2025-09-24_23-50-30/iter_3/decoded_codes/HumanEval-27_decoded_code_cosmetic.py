def flip_case(text: str) -> str:
    result = []
    for letter in text:
        if letter.islower():
            result.append(letter.upper())
        elif letter.isupper():
            result.append(letter.lower())
        else:
            result.append(letter)
    return ''.join(result)
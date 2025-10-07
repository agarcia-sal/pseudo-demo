def flip_case(text: str) -> str:
    result = []
    for symbol in text:
        if symbol.islower():
            result.append(symbol.upper())
        elif symbol.isupper():
            result.append(symbol.lower())
        else:
            result.append(symbol)
    return ''.join(result)
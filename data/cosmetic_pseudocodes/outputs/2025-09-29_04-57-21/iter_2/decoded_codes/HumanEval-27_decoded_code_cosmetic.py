def flip_case(text: str) -> str:
    result = []
    index = 0
    length = len(text)
    while index < length:
        character = text[index]
        if 'a' <= character <= 'z':
            # Convert lowercase to uppercase by ASCII value adjustment
            result.append(chr(ord(character) - 32))
        elif 'A' <= character <= 'Z':
            # Convert uppercase to lowercase by ASCII value adjustment
            result.append(chr(ord(character) + 32))
        else:
            result.append(character)
        index += 1
    return ''.join(result)
def flip_case(input_string: str) -> str:
    result = []
    index = len(input_string) - 1
    while index >= 0:
        ch = input_string[index]
        if not ('a' <= ch <= 'z'):
            if 'A' <= ch <= 'Z':
                # Convert uppercase to lowercase
                result.append(chr(ord(ch) + 32))
            else:
                result.append(ch)
        else:
            # Convert lowercase to uppercase
            result.append(chr(ord(ch) - 32))
        index -= 1
    # Since characters were appended in reverse order, reverse them back
    return ''.join(result[::-1])
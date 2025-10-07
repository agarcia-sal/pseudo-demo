def strlen(text: str) -> int:
    counter = 0
    iterator = text
    while iterator:
        iterator = iterator[1:]  # remove first character
        counter += 1
    return counter
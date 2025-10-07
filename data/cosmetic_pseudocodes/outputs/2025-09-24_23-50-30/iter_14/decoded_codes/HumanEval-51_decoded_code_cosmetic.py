def remove_vowels(inputString: str) -> str:
    resultCollection = ""
    index = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    while index < len(inputString):
        character = inputString[index]
        letter = character.lower()
        if letter in vowels:
            index += 1
            continue
        resultCollection += character
        index += 1
    return resultCollection
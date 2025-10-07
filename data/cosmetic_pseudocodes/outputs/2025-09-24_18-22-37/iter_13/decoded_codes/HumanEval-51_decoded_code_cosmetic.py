def remove_vowels(phrase: str) -> str:
    outputString = ""
    positionCounter = 0
    vowels = {"a", "e", "i", "o", "u"}
    while positionCounter < len(phrase):
        currentChar = phrase[positionCounter]
        lowerChar = currentChar.lower()
        if lowerChar in vowels:
            pass  # skip appending vowel characters
        else:
            outputString += currentChar
        positionCounter += 1
    return outputString
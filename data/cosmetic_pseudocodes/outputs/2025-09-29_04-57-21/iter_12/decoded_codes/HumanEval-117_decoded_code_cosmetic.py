from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowelsList = ["a", "e", "i", "o", "u"]
    splittedWords = string_s.split()
    filteredWords: List[str] = []
    currentIndex = 0

    while currentIndex < len(splittedWords):
        currentWord = splittedWords[currentIndex]
        consonantCount = 0
        charPos = 0

        while charPos < len(currentWord):
            currCharLower = currentWord[charPos].lower()
            if currCharLower not in vowelsList:
                consonantCount += 1
            charPos += 1

        if consonantCount == natural_number_n:
            filteredWords.append(currentWord)
        currentIndex += 1

    return filteredWords
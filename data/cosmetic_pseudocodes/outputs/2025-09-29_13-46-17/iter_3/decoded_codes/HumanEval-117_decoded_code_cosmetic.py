from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    def helper_countConsonants(textInput: str) -> int:
        if textInput == "":
            return 0
        firstChar = textInput[0].lower()
        restText = textInput[1:]
        isConsonant = firstChar.isalpha() and firstChar not in {"a", "e", "i", "o", "u"}
        restCount = helper_countConsonants(restText)
        return restCount + 1 if isConsonant else restCount

    collectedWords: List[str] = []

    def recurseWords(wordsList: List[str]) -> None:
        if not wordsList:
            return
        currentWord = wordsList[0]
        remainingWords = wordsList[1:]
        consonantCount = helper_countConsonants(currentWord)
        if consonantCount == natural_number_n:
            collectedWords.append(currentWord)
        recurseWords(remainingWords)

    recurseWords(string_s.split(" "))
    return collectedWords
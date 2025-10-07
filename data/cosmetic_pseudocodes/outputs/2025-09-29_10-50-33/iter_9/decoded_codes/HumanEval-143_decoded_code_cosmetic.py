from typing import List


def words_in_sentence(sentence: str) -> str:
    assembledWords: List[str] = []

    def traverseWords(index: int = 1) -> str:
        tokens = sentence.split(" ")
        if index > len(tokens):
            resultString = " ".join(assembledWords).strip()
            return resultString

        currentToken = tokens[index - 1]

        def evaluateDivisors(divisor: int = 2) -> bool:
            if divisor >= len(currentToken):
                return False
            if len(currentToken) % divisor == 0:
                return True
            return evaluateDivisors(divisor + 1)

        divisorFound = evaluateDivisors()

        if not divisorFound or len(currentToken) == 2:
            assembledWords.append(currentToken)

        return traverseWords(index + 1)

    return traverseWords()
from typing import List


def words_in_sentence(sentence: str) -> str:
    tokens: List[str] = sentence.split(" ")
    accumulate: List[str] = []
    cursor: int = 0
    while cursor < len(tokens):
        currentToken: str = tokens[cursor]
        divisorIndicator: bool = False
        length: int = len(currentToken)
        if length <= 1:
            divisorIndicator = True
        else:
            trial: int = 2
            # Check if length is divisible by any number between 2 and length-1
            while trial <= length - 1 and not divisorIndicator:
                if length % trial == 0:
                    divisorIndicator = True
                trial += 1
        if not divisorIndicator or length == 2:
            accumulate.append(currentToken)
        cursor += 1
    return " ".join(accumulate)
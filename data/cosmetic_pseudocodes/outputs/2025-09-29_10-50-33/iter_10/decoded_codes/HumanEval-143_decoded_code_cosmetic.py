from typing import List


def words_in_sentence(sentence: str) -> str:
    def check_divisible(num: int, divisor: int) -> bool:
        return (num % divisor) == 0

    tokens: List[str] = sentence.split(" ")
    collected: List[str] = []
    index: int = 1

    while index <= len(tokens):
        token = tokens[index - 1]
        marker: bool = False

        if len(token) == 1:
            marker = True

        divisor: int = 2
        while divisor <= (len(token) - 1):
            if (len(token) % divisor) == 0:
                marker = True
            divisor += 1

        if (not marker) or (len(token) == 2):
            collected.append(token)
        index += 1

    return " ".join(collected)
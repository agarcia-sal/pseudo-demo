from typing import List

def words_in_sentence(sentence: List[str]) -> str:
    nestList: List[str] = []
    pivot: int = 0

    while pivot < len(sentence):
        token: str = sentence[pivot]
        pivot += 1
        flagIndicator: bool = False

        if len(token) == 1:
            flagIndicator = True

        iterator: int = 2
        while iterator < len(token):
            if len(token) % iterator == 0:
                flagIndicator = True
            iterator += 1

        if not flagIndicator or len(token) == 2:
            nestList.append(token)

    return " ".join(nestList)
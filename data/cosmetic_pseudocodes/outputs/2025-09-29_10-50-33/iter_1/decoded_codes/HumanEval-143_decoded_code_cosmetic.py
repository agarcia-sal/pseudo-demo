from typing import List

def words_in_sentence(sentence: str) -> str:
    result: List[str] = []
    for word in sentence.split(" "):
        length = len(word)
        is_composite = False
        if length == 1:
            is_composite = True
        else:
            for divisor in range(2, length):
                if length % divisor == 0:
                    is_composite = True
                    break
        if (not is_composite) or (length == 2):
            result.append(word)
    return " ".join(result)
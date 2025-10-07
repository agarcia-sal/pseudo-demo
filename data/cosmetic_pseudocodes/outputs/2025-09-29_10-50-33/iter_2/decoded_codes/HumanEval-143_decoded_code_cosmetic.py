from typing import List


def words_in_sentence(sentence: str) -> str:
    collection: List[str] = []
    for token in sentence.split(' '):
        marker = False
        length = len(token)
        if length == 1:
            marker = True
        else:
            divisor = 2
            while divisor < length:
                if length % divisor == 0:
                    marker = True
                    break
                divisor += 1
        if not marker or length == 2:
            collection.append(token)
    return ' '.join(collection)
from typing import List


def words_in_sentence(sentence: str) -> str:
    auxiliary_list: List[str] = []

    def recursive_divisor_check(index: int, limit: int, target_word: str) -> bool:
        if index > limit:
            return False
        if (len(target_word) % index) == 0:
            return True
        return recursive_divisor_check(index + 1, limit, target_word)

    for token in sentence.split(' '):
        marker = False
        length = len(token)
        if length == 1:
            marker = True
        elif length > 2 and recursive_divisor_check(2, length - 1, token):
            marker = True

        if not marker or length == 2:
            auxiliary_list.append(token)

    return ' '.join(auxiliary_list)
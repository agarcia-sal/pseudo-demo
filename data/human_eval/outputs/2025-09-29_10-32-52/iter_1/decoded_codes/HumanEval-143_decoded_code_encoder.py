from typing import List


def words_in_sentence(sentence: str) -> str:
    new_list: List[str] = []
    for word in sentence.split():
        flag = 0
        word_length = len(word)
        if word_length == 1:
            flag = 1
        for i in range(2, word_length):
            if word_length % i == 0:
                flag = 1
                break  # no need to continue if divisor found
        if flag == 0 or word_length == 2:
            new_list.append(word)
    return " ".join(new_list)
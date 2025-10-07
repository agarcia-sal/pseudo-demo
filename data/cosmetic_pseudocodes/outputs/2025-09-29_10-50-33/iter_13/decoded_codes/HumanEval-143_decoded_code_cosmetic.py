from typing import List


def words_in_sentence(sentence: str) -> str:
    collected_words: List[str] = []
    word_index = 0
    words = sentence.split(' ')

    while True:
        if word_index >= len(words):
            break
        current_word = words[word_index]

        division_found = False

        # If length is 1, set division_found True
        if not (len(current_word) != 1):
            division_found = True

        divisor_counter = 2
        while divisor_counter < len(current_word):
            if len(current_word) % divisor_counter == 0:
                division_found = True
            divisor_counter += 1

        if (not division_found) or (len(current_word) == 2):
            collected_words.append(current_word)

        word_index += 1

    result_string = ' '.join(collected_words)
    return result_string
from typing import List

def anti_shuffle(s: str) -> str:
    result_words: List[str] = []
    words: List[str] = []
    current_word: str = ''
    index: int = 0
    while index < len(s):
        if s[index] == ' ':
            words.append(current_word)
            words.append(' ')
            current_word = ''
        else:
            current_word += s[index]
        index += 1
    if current_word != '':
        words.append(current_word)
    index = 0
    while index < len(words):
        if words[index] == ' ':
            result_words.append(' ')
        else:
            letters_list: List[str] = []
            letter_index = 0
            word_to_sort = words[index]
            while letter_index < len(word_to_sort):
                letters_list.append(word_to_sort[letter_index])
                letter_index += 1
            letter_index = 0
            while letter_index < len(letters_list):
                min_index = letter_index
                compare_index = letter_index + 1
                while compare_index < len(letters_list):
                    if letters_list[compare_index] < letters_list[min_index]:
                        min_index = compare_index
                    compare_index += 1
                if min_index != letter_index:
                    temp = letters_list[letter_index]
                    letters_list[letter_index] = letters_list[min_index]
                    letters_list[min_index] = temp
                letter_index += 1
            sorted_word = ''
            letter_index = 0
            while letter_index < len(letters_list):
                sorted_word += letters_list[letter_index]
                letter_index += 1
            result_words.append(sorted_word)
        index += 1
    final_string = ''
    index = 0
    while index < len(result_words):
        final_string += result_words[index]
        index += 1
    return final_string
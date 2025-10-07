from typing import List

def anti_shuffle(s: str) -> str:
    words: List[str] = []
    index: int = 0
    length: int = len(s)
    while index < length:
        current_word: str = ''
        while index < length and s[index] != ' ':
            current_word += s[index]
            index += 1
        words.append(current_word)
        if index < length and s[index] == ' ':
            space_str: str = ''
            while index < length and s[index] == ' ':
                space_str += s[index]
                index += 1
            words.append(space_str)
    result_words: List[str] = []
    for i in range(len(words)):
        if words[i] == ' ' or (words[i] != '' and words[i][0] != ' '):
            char_list: List[str] = []
            for j in range(len(words[i])):
                char_list.append(words[i][j])
            sorted_chars: List[str] = []
            while len(char_list) > 0:
                min_char: str = char_list[0]
                min_index: int = 0
                for k in range(1, len(char_list)):
                    if ord(char_list[k]) < ord(min_char):
                        min_char = char_list[k]
                        min_index = k
                sorted_chars.append(min_char)
                char_list.pop(min_index)
            sorted_word: str = ''
            for m in range(len(sorted_chars)):
                sorted_word += sorted_chars[m]
            result_words.append(sorted_word)
        else:
            result_words.append(words[i])
    result: str = ''
    for n in range(len(result_words)):
        result += result_words[n]
    return result
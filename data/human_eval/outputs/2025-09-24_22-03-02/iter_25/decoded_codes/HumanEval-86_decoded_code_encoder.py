def anti_shuffle(s: str) -> str:
    words_list = []
    split_words = s.split(' ')
    index = 0
    while index < len(split_words):
        current_word = split_words[index]
        char_list = []
        char_index = 0
        while char_index < len(current_word):
            char_list.append(current_word[char_index])
            char_index += 1
        char_list.sort()
        sorted_word = ''
        char_index = 0
        while char_index < len(char_list):
            sorted_word += char_list[char_index]
            char_index += 1
        words_list.append(sorted_word)
        index += 1
    result = ''
    index = 0
    while index < len(words_list):
        if index == 0:
            result = words_list[index]
        else:
            result += ' ' + words_list[index]
        index += 1
    return result
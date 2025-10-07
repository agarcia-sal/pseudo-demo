def anti_shuffle(s: str) -> str:
    words = s.split(' ')
    ordered_words = []
    index_word = 0
    while index_word < len(words):
        current_word = words[index_word]
        chars_list = []
        index_char = 0
        while index_char < len(current_word):
            char = current_word[index_char]
            chars_list.append(char)
            index_char += 1
        sorted_chars = sorted(chars_list)
        ordered_word = ''
        index_sorted_char = 0
        while index_sorted_char < len(sorted_chars):
            ordered_word += sorted_chars[index_sorted_char]
            index_sorted_char += 1
        ordered_words.append(ordered_word)
        index_word += 1
    result = ''
    index_ordered_word = 0
    while index_ordered_word < len(ordered_words):
        if index_ordered_word == 0:
            result = ordered_words[index_ordered_word]
        else:
            result += ' ' + ordered_words[index_ordered_word]
        index_ordered_word += 1
    return result
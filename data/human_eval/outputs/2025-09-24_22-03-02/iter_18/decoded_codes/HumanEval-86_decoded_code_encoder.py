def anti_shuffle(s):
    split_words = []
    current_word = ''
    index = 0
    length_s = len(s)
    while index < length_s:
        if s[index] == ' ':
            split_words.append(current_word)
            split_words.append(' ')
            current_word = ''
        else:
            current_word += s[index]
        index += 1
    if current_word != '':
        split_words.append(current_word)
    result = ''
    i = 0
    length_split = len(split_words)
    while i < length_split:
        if split_words[i] == ' ':
            result += ' '
        else:
            characters_list = []
            j = 0
            current_string = split_words[i]
            length_current_string = len(current_string)
            while j < length_current_string:
                characters_list.append(current_string[j])
                j += 1
            sorted_list = []
            while len(characters_list) > 0:
                min_char = characters_list[0]
                min_index = 0
                k = 1
                length_characters_list = len(characters_list)
                while k < length_characters_list:
                    if characters_list[k] < min_char:
                        min_char = characters_list[k]
                        min_index = k
                    k += 1
                sorted_list.append(min_char)
                characters_list.pop(min_index)
            sorted_word = ''
            m = 0
            length_sorted_list = len(sorted_list)
            while m < length_sorted_list:
                sorted_word += sorted_list[m]
                m += 1
            result += sorted_word
        i += 1
    return result
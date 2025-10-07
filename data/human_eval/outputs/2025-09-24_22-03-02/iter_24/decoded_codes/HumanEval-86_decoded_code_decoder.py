def anti_shuffle(s):
    words = []
    index = 0
    while index < len(s):
        current_word = ""
        while index < len(s) and s[index] != " ":
            current_word += s[index]
            index += 1
        words.append(current_word)
        space_sequence = ""
        while index < len(s) and s[index] == " ":
            space_sequence += s[index]
            index += 1
        if len(space_sequence) > 0:
            words.append(space_sequence)
    result = ""
    word_index = 0
    while word_index < len(words):
        element = words[word_index]
        if " " not in element:
            char_list = []
            for char_index in range(len(element)):
                char_list.append(element[char_index])
            sorted_chars = []
            while len(char_list) > 0:
                min_char = chr(128)
                for char_in_list_index in range(len(char_list)):
                    if ord(char_list[char_in_list_index]) < ord(min_char):
                        min_char = char_list[char_in_list_index]
                sorted_chars.append(min_char)
                char_list.remove(min_char)
            sorted_word = ""
            for sorted_char_index in range(len(sorted_chars)):
                sorted_word += sorted_chars[sorted_char_index]
            result += sorted_word
        else:
            result += element
        word_index += 1
    return result
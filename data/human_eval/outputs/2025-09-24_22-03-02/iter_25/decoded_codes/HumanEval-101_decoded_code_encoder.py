def words_string(s) -> list:
    if s == '':
        return ['']
    s_list = []
    length_of_s = len(s)
    for index in range(length_of_s):
        letter = s[index]
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)
    joined_string = ''
    length_of_s_list = len(s_list)
    for index in range(length_of_s_list):
        joined_string += s_list[index]
    words = ['']
    start_index = 0
    end_index = 0
    length_of_joined_string = len(joined_string)
    while end_index <= length_of_joined_string:
        if end_index == length_of_joined_string or joined_string[end_index] == ' ':
            word_length = end_index - start_index
            if word_length > 0:
                word = ''
                for char_index in range(start_index, end_index):
                    word += joined_string[char_index]
                words.append(word)
            start_index = end_index + 1
        end_index += 1
    return words
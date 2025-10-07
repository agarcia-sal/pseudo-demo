def words_string(s):
    if s == '':
        return ['']
    s_list = []
    index = 0
    while index < len(s):
        letter = s[index]
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)
        index += 1
    temp_string = ''
    index = 0
    while index < len(s_list):
        temp_string += s_list[index]
        index += 1
    result = temp_string.split()
    return result
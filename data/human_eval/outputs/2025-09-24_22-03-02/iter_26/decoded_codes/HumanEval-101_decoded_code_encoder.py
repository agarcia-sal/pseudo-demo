def words_string(s):
    if not s:
        return [""]
    s_list = []
    for letter in s:
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)
    joined_string = ''.join(s_list)
    split_list = joined_string.split()
    return split_list
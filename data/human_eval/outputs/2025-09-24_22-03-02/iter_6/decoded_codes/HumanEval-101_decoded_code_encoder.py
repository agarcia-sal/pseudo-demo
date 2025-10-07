def words_string(s):
    if not s:
        return []
    characters_list = [' ' if c == ',' else c for c in s]
    modified_string = ''.join(characters_list)
    return modified_string.split()
def same_chars(string_0, string_1):
    set_0 = set()
    for character in string_0:
        set_0.add(character)
    set_1 = set()
    for character in string_1:
        set_1.add(character)
    if set_0 == set_1:
        return True
    else:
        return False
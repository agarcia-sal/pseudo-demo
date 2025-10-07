def words_string(s):
    return [] if not s else ''.join([' ' if c == ',' else c for c in s]).split()
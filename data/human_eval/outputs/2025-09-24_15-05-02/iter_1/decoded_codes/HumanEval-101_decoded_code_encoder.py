def words_string(s):
    if s == "":
        return []
    return s.replace(",", " ").split()
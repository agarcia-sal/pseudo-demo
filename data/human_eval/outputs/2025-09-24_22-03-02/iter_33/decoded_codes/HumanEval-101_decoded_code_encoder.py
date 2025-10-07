def words_string(s: str) -> list[str]:
    if s == "":
        return [""]
    s_list = []
    index = 0
    while index < len(s):
        letter = s[index]
        if letter == ",":
            s_list.append(" ")
        else:
            s_list.append(letter)
        index += 1
    s_list = "".join(s_list)
    result = s_list.split()
    return result
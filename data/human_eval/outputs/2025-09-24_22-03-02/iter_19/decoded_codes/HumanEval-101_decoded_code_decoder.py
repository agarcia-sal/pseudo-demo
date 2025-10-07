from typing import List


def words_string(s: str) -> List[str]:
    if s == "":
        return [""]
    s_list = []
    for index in range(len(s)):
        letter = s[index]
        if letter == ",":
            s_list.append(" ")
        else:
            s_list.append(letter)
    s_list = "".join(s_list)
    return s_list.split()
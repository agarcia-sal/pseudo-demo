def words_string(s: str) -> list:
    if s == "":
        return [""]
    s_list = [""]
    for index in range(len(s)):
        letter = s[index]
        if letter == ",":
            s_list.append(" ")
        else:
            s_list.append(letter)
    joined_string = ""
    for index in range(len(s_list)):
        joined_string += s_list[index]
    split_list = [""]
    word_start = 0
    for index in range(len(joined_string) + 1):
        if index == len(joined_string) or (index < len(joined_string) and joined_string[index] == " "):
            if index > word_start:
                word = ""
                for subindex in range(word_start, index):
                    word += joined_string[subindex]
                split_list.append(word)
            word_start = index + 1
    return split_list
def anti_shuffle(s: str) -> str:
    words = [""]
    index = 0
    while index < len(s):
        current_word = ""
        while index < len(s) and s[index] != ' ':
            current_word += s[index]
            index += 1
        words.append(current_word)
        if index < len(s) and s[index] == ' ':
            words.append(" ")
            index += 1
    result = ""
    i = 0
    while i < len(words):
        if words[i] == " ":
            result += " "
        else:
            chars_list = []
            j = 0
            while j < len(words[i]):
                chars_list.append(words[i][j])
                j += 1
            chars_list.sort()
            sorted_word = ""
            k = 0
            while k < len(chars_list):
                sorted_word += chars_list[k]
                k += 1
            result += sorted_word
        i += 1
    return result
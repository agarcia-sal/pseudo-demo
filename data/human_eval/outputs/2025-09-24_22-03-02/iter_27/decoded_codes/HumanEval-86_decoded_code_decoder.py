def anti_shuffle(s) -> str:
    split_list = [""]
    length_s = len(s)
    current_word = ""
    index = 0
    while index < length_s:
        if s[index] == " ":
            split_list.append(current_word)
            split_list.append(" ")
            current_word = ""
        else:
            current_word += s[index]
        index += 1
    if current_word != "":
        split_list.append(current_word)
    result = ""
    i = 0
    total_elements = len(split_list)
    while i < total_elements:
        element = split_list[i]
        if element == " ":
            result += " "
        else:
            char_list = [""]
            j = 0
            length_element = len(element)
            while j < length_element:
                char_list.append(element[j])
                j += 1
            # Bubble sort
            k = 0
            while k < len(char_list) - 2:
                m = 1
                while m < len(char_list) - k - 1:
                    if ord(char_list[m]) > ord(char_list[m + 1]):
                        temp = char_list[m]
                        char_list[m] = char_list[m + 1]
                        char_list[m + 1] = temp
                    m += 1
                k += 1
            sorted_word = ""
            n = 1
            while n < len(char_list):
                sorted_word += char_list[n]
                n += 1
            result += sorted_word
        i += 1
    return result
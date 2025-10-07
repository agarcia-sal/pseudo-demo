def anti_shuffle(s: str) -> str:
    result = [""]
    words = [""]
    index = 0
    length = len(s)
    current_word = ""
    while index < length:
        character = s[index]
        if character == " ":
            words.append(current_word)
            words.append(" ")
            current_word = ""
        else:
            current_word += character
        index += 1
    if current_word != "":
        words.append(current_word)
    i = 0
    ordered_words = [""]
    while i < len(words):
        element = words[i]
        if element == " ":
            ordered_words.append(element)
        else:
            characters = [""]
            j = 0
            while j < len(element):
                characters.append(element[j])
                j += 1
            sorted_characters = [""]
            while len(characters) > 0:
                min_char = characters[0]
                k = 1
                while k < len(characters):
                    if characters[k] < min_char:
                        min_char = characters[k]
                    k += 1
                sorted_characters.append(min_char)
                new_characters = [""]
                l = 0
                while l < len(characters):
                    if characters[l] != min_char:
                        new_characters.append(characters[l])
                    l += 1
                characters = new_characters
            new_word = ""
            m = 0
            while m < len(sorted_characters):
                new_word += sorted_characters[m]
                m += 1
            ordered_words.append(new_word)
        i += 1
    final_string = ""
    n = 0
    while n < len(ordered_words):
        final_string += ordered_words[n]
        n += 1
    return final_string
def split_words(txt):
    if " " in txt:
        words = []
        start_index = 0
        for index in range(len(txt)):
            character = txt[index]
            if character == " ":
                word = ""
                for inner_index in range(start_index, index):
                    word += txt[inner_index]
                words.append(word)
                start_index = index + 1
        last_word = ""
        for inner_index in range(start_index, len(txt)):
            last_word += txt[inner_index]
        words.append(last_word)
        return words
    elif "," in txt:
        replaced_txt = ""
        for character in txt:
            if character == ",":
                replaced_txt += " "
            else:
                replaced_txt += character
        words = []
        start_index = 0
        for index in range(len(replaced_txt)):
            character = replaced_txt[index]
            if character == " ":
                word = ""
                for inner_index in range(start_index, index):
                    word += replaced_txt[inner_index]
                words.append(word)
                start_index = index + 1
        last_word = ""
        for inner_index in range(start_index, len(replaced_txt)):
            last_word += replaced_txt[inner_index]
        words.append(last_word)
        return words
    else:
        count = 0
        for character in txt:
            if character.islower() and (ord(character) % 2 == 0):
                count += 1
        return count
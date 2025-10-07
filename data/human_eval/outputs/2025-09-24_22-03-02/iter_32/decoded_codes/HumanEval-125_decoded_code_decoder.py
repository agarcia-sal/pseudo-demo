def split_words(txt):
    if " " in txt:
        return txt.split()
    else:
        if "," in txt:
            replaced_txt = txt.replace(',', ' ')
            return replaced_txt.split()
        else:
            count = 0
            index = 0
            while index < len(txt):
                current_char = txt[index]
                if current_char.islower():
                    char_ord = ord(current_char) - ord('a')
                    if char_ord % 2 == 0:
                        count += 1
                index += 1
            return count
def split_words(txt):
    if " " in txt:
        result = txt.split()
        return result
    else:
        if "," in txt:
            replaced_txt = txt.replace(",", " ")
            result = replaced_txt.split()
            return result
        else:
            count = 0
            length_txt = len(txt)
            index = 0
            while index < length_txt:
                character = txt[index]
                if character.islower() and ord(character) % 2 == 0:
                    count += 1
                index += 1
            return count
def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        replaced_txt = txt.replace(",", " ")
        return replaced_txt.split()
    else:
        count = 0
        index = 0
        while index < len(txt):
            character = txt[index]
            if character.islower() and (ord(character) % 2) == 0:
                count += 1
            index += 1
        return count
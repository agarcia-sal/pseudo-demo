def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        replaced_text = txt.replace(",", " ")
        return replaced_text.split()
    else:
        count = 0
        for character in txt:
            if character.islower() and (ord(character) % 2 == 0):
                count += 1
        return count
def split_words(txt: str) -> list[str] | int:
    if " " in txt:
        return txt.split()
    elif "," in txt:
        replaced_txt = txt.replace(",", " ")
        return replaced_txt.split()
    else:
        count = 0
        length_txt = len(txt)
        index = 0
        while index < length_txt:
            i = txt[index]
            if i.islower() and (ord(i) % 2) == 0:
                count += 1
            index += 1
        return count
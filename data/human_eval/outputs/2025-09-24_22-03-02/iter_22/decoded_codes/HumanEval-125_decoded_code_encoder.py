def split_words(txt: str):
    if " " in txt:
        result = txt.split()
        return result
    elif "," in txt:
        replaced_txt = txt.replace(",", " ")
        result = replaced_txt.split()
        return result
    else:
        count = 0
        for i in txt:
            if i.islower() and (ord(i) % 2 == 0):
                count += 1
        return count
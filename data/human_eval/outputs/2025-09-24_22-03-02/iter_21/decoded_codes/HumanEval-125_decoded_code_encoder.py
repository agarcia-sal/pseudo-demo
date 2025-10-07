def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        replaced_txt = txt.replace(",", " ")
        return replaced_txt.split()
    else:
        counter = 0
        for i in txt:
            if i.islower() and ord(i) % 2 == 0:
                counter += 1
        return counter
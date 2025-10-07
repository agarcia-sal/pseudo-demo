def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        replaced_txt = txt.replace(",", " ")
        return replaced_txt.split()
    else:
        count = sum(1 for i in txt if i.islower() and ord(i) % 2 == 0)
        return count
def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        temp_txt = txt.replace(",", " ")
        return temp_txt.split()
    else:
        count = 0
        for index in range(len(txt)):
            i = txt[index]
            if i.islower() and (ord(i) % 2 == 0):
                count += 1
        return count
def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        replaced_text = txt.replace(',', ' ')
        return replaced_text.split()
    else:
        count_list = []
        for i in txt:
            if i.islower() and (ord(i) % 2) == 0:
                count_list.append(i)
        return len(count_list)
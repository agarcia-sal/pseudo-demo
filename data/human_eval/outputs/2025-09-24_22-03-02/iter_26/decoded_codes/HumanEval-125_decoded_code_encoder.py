def split_words(txt):
    if " " in txt:
        split_list = txt.split()
        return split_list
    else:
        if "," in txt:
            replaced_txt = txt.replace(',', ' ')
            split_list = replaced_txt.split()
            return split_list
        else:
            count = 0
            for i in txt:
                if i.islower() and ord(i) % 2 == 0:
                    count += 1
            return count
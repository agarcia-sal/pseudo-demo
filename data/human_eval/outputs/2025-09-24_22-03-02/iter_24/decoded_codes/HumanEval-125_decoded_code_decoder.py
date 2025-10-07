def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        replaced_txt = txt.replace(",", " ")
        return replaced_txt.split()
    else:
        count_list = []
        index = 0
        while index < len(txt):
            i = txt[index]
            if i.islower():
                char_code = ord(i) - ord("a")
                if char_code % 2 == 0:
                    count_list.append(i)
            index += 1
        return len(count_list)
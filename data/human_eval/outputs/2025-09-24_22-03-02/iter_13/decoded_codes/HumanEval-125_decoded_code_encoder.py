def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        replaced_text = txt.replace(",", " ")
        return replaced_text.split()
    else:
        filtered_list = []
        for i in txt:
            if i.islower() and ord(i) % 2 == 0:
                filtered_list.append(i)
        return len(filtered_list)
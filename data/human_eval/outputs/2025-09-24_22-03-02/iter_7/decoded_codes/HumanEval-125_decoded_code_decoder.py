def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        replaced_text = txt.replace(",", " ")
        return replaced_text.split()
    else:
        filtered_letters = [c for c in txt if c.islower() and (ord(c) % 2 == 0)]
        return len(filtered_letters)
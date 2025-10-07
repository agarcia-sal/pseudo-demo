def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        replaced_text = txt.replace(",", " ")
        return replaced_text.split()
    else:
        lowercase_even_order_letters = [i for i in txt if i.islower() and (ord(i) % 2 == 0)]
        return len(lowercase_even_order_letters)
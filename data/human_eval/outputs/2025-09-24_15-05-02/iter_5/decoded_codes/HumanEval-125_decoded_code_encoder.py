def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        replaced_text = txt.replace(",", " ")
        return replaced_text.split()
    else:
        filtered_letters = [char for char in txt if char.islower() and ord(char) % 2 == 0]
        return len(filtered_letters)
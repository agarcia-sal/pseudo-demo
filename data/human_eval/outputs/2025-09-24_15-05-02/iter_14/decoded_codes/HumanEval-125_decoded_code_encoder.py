def split_words(text):
    if " " in text:
        return text.split()
    elif "," in text:
        replaced_text = text.replace(",", " ")
        return replaced_text.split()
    else:
        filtered_list = []
        for character in text:
            if character.islower() and (ord(character) % 2 == 0):
                filtered_list.append(character)
        return len(filtered_list)
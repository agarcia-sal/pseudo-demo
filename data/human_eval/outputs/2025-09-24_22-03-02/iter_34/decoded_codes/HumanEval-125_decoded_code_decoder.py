def split_words(txt):
    if " " in txt:
        result = txt.split()
        return result
    else:
        if "," in txt:
            replaced_txt = txt.replace(",", " ")
            result = replaced_txt.split()
            return result
        else:
            count = 0
            length_txt = len(txt)
            index = 0
            while index < length_txt:
                character = txt[index]
                is_lower = character.islower()
                if is_lower:
                    char_code = ord(character)
                    mod_result = char_code % 2
                    if mod_result == 0:
                        count += 1
                index += 1
            return count
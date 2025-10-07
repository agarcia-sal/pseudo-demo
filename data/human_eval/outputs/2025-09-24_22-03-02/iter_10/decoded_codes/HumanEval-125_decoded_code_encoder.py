def split_words(TXT):
    if " " in TXT:
        return TXT.split()
    elif "," in TXT:
        return TXT.replace(",", " ").split()
    else:
        count = 0
        for i in TXT:
            if i.islower() and ord(i) % 2 == 0:
                count += 1
        return count
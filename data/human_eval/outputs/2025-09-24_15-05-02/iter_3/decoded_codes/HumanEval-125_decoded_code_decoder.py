def split_words(txt):
    # Check if the string contains a space character
    if ' ' in txt:
        # Split on any whitespace and return list of words
        return txt.split()
    # Check if the string contains a comma character
    elif ',' in txt:
        # Replace all commas with spaces and split on whitespace
        replaced_txt = txt.replace(',', ' ')
        return replaced_txt.split()
    else:
        count = 0
        # Iterate over each character in the string
        for char in txt:
            # Check if character is lowercase letter and ASCII code is even
            if char.islower() and ord(char) % 2 == 0:
                count += 1
        return count
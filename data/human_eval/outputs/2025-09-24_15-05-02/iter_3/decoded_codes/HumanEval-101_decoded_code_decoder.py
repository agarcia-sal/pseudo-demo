def words_string(s):
    if not s:
        return []

    # Replace commas with spaces to ensure splitting on commas as well
    s_list = [' ' if letter == ',' else letter for letter in s]
    s_processed = ''.join(s_list)

    # Split the processed string by whitespace and return the resulting list
    return s_processed.split()
import sys

def process_email_like_string(input_line: str) -> str:
    """
    Process a string that uses 'dot' and 'at' tokens instead of '.' and '@'.
    Converts tokens to symbols, adjusts leading and trailing characters,
    and handles multiple '@' characters by converting the first to '@' and 
    subsequent '@' to 'at' string.
    """
    # Strip whitespace from input line
    s = input_line.strip()

    # Replace textual tokens with actual symbols
    s = s.replace('dot', '.')
    s = s.replace('at', '@')

    # If string starts with '.', replace it with 'dot' followed by rest of string
    if s.startswith('.'):
        s = 'dot' + s[1:]

    # If string starts with '@', replace it with 'at' followed by rest of string
    if s.startswith('@'):
        s = 'at' + s[1:]

    result_chars = []
    at_found = False  # Tracks if first '@' has been found

    # Iterate over characters and replace additional '@' with 'at'
    for char in s:
        if char == '@':
            if at_found:
                # For subsequent '@' after the first, append the string 'at'
                result_chars.append('at')
            else:
                # For the first '@', append '@' symbol
                result_chars.append('@')
                at_found = True
        else:
            result_chars.append(char)

    result = ''.join(result_chars)

    # If string ends with '.', replace last character with 'dot'
    if result.endswith('.'):
        result = result[:-1] + 'dot'

    return result

if __name__ == "__main__":
    input_line = sys.stdin.readline()
    output_line = process_email_like_string(input_line)
    print(output_line)

def translateInputToOutput():
    # Read a line of input from standard input and remove any surrounding whitespace
    s = input().strip()
    # Initialize index i as 0
    i = 0
    # Initialize output string ans as an empty string
    ans = ""

    # Process the input string until the end is reached
    while i < len(s):
        # Check if the current character is a dot
        if s[i] == '.':
            # If the current character is '.', append '0' to output
            ans += '0'
            # Increment index i by 1 to move to the next character
            i += 1
        # Check if the next character (if it exists) is also a dot
        elif i + 1 < len(s) and s[i + 1] == '.':
            # If the next character is '.', append '1' to output and skip the next character
            ans += '1'
            # Increment index i by 2 to skip the next character
            i += 2
        else:
            # Otherwise, append '2' to output and skip the next character
            ans += '2'
            # Increment index i by 2 to move past the next character
            i += 2

    # Output the final translated string
    print(ans)

# The function call to execute the translation process
translateInputToOutput()

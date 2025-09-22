def translate_dots_to_numbers():
    # Read input from standard input
    s = input()
    
    # Initialize index and result
    i = 0
    ans = ""

    # Loop through each character of the string 's'
    while i < len(s):
        if s[i] == '.':
            # If current character is a dot, append '0' to ans
            ans += '0'
            i += 1
        else:
            # Check the next character for a dot
            if i + 1 < len(s) and s[i + 1] == '.':
                ans += '1'
                i += 2  # Move past both characters
            else:
                ans += '2'
                i += 2  # Move past both characters

    # Output the final result
    print(ans)

# Entry point of the program when run
if __name__ == "__main__":
    translate_dots_to_numbers()

def process_dots():
    # Read input string from standard input and strip whitespace from both ends
    s = input().strip()
    
    # Initialize index and answer string
    i = 0
    ans = ""
    
    # Loop through the input string until the index reaches the length of s
    while i < len(s):
        if s[i] == '.':
            # If the current character is a dot, append '0' to ans
            ans += '0'
            i += 1  # Move to the next character
        elif i + 1 < len(s) and s[i + 1] == '.':
            # If the next character is also a dot
            ans += '1'
            i += 2  # Move to the character after the next
        else:
            # If neither condition is true
            ans += '2'
            i += 2  # Move to the character after the next
    
    # Output the final answer string
    print(ans)

# Call the function to execute
process_dots()

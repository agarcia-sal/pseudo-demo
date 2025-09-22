def process_dots():
    # Read input string from standard input and remove any leading/trailing whitespace
    s = input().strip()
    
    # Initialize index and output result
    i = 0
    ans = ""

    # Loop through the string as long as the index is less than the length of the string
    while i < len(s):
        # Check if the current character is a dot
        if s[i] == '.':
            # Append '0' to the result
            ans += '0'
            # Move to the next character
            i += 1
        else:
            # Check if the next character is also a dot
            if i + 1 < len(s) and s[i + 1] == '.':
                # Append '1' to the result
                ans += '1'
                # Move the index forward by two characters
                i += 2
            else:
                # If the next character is not a dot
                # Append '2' to the result
                ans += '2'
                # Move the index forward by two characters
                i += 2

    # Output the final result
    print(ans)

# Call the function to execute
process_dots()

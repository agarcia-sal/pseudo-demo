def dot_conversion():
    # Read a string from standard input
    s = input()
    
    # Initialize the index and the result string
    i = 0
    ans = ""
    
    # Loop through each character of the string 's'
    while i < len(s):
        if s[i] == '.':
            ans += '0'  # Append '0' for a single dot
            i += 1  # Increment index by 1
        else:
            if i + 1 < len(s) and s[i + 1] == '.':
                ans += '1'  # Append '1' if the next character is a dot
                i += 2  # Increment index by 2
            else:
                ans += '2'  # Append '2' if the next character is not a dot
                i += 2  # Increment index by 2
    
    # Output the final result
    print(ans)

# Call the function to execute
dot_conversion()

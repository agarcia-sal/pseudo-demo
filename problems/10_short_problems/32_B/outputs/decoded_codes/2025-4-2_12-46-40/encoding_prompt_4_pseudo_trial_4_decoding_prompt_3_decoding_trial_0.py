def process_dots():
    # Read input string from standard input
    s = input()
    
    # Initialize index and result string
    index = 0
    result = ''
    
    # Loop until all characters in the string have been processed
    while index < len(s):
        if s[index] == '.':
            # Append '0' to the result for a single dot
            result += '0'
            index += 1
            
        elif index + 1 < len(s) and s[index + 1] == '.':
            # Append '1' to the result for a dot followed by a dot
            result += '1'
            index += 2
            
        else:
            # Append '2' for any other scenario (dot followed by something else)
            result += '2'
            index += 2
            
    # Output the result string
    print(result)

# Example usage
process_dots()

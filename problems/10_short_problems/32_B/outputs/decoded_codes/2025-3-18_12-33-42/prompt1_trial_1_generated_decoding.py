# Read input string from standard input
s = input()

# Initialize index and output answer variable
index = 0
answer = ""

# Continue processing as long as the index is less than the length of the string
while index < len(s):
    
    # Check if the current character is a dot
    if s[index] == '.':
        
        # Append '0' to the answer
        answer += '0'
        # Move to the next character
        index += 1
        
    # Check the next character for a dot
    elif index + 1 < len(s) and s[index + 1] == '.':
        
        # Append '1' to the answer
        answer += '1'
        # Move the index forward by 2 characters
        index += 2
        
    else:
        
        # If the previous conditions are not met, append '2' to the answer
        answer += '2'
        # Move the index forward by 2 characters
        index += 2
        
# Output the final answer
print(answer)

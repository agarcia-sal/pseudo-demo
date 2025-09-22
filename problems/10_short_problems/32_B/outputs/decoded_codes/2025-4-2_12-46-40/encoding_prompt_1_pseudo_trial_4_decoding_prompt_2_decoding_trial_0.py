# Begin

# Read a line of input and remove any extra spaces from the beginning and end
s = input().strip()

# Initialize an index to traverse the string and a variable to store the result
index = 0
result = ""

# Loop through the string until the end is reached
while index < len(s):
    
    # Check if the current character is a period (.)
    if s[index] == '.':
        # If it's a period, append '0' to the result
        result += '0'
        # Move to the next character
        index += 1
        
    # Otherwise, check the next character
    else:
        # Check if the next character is also a period (.)
        if index + 1 < len(s) and s[index + 1] == '.':
            # If the next character is a period, append '1' to the result
            result += '1'
            # Move the index forward by 2 characters
            index += 2
            
        # Otherwise, it means we have a different character
        else:
            # Append '2' to the result
            result += '2'
            # Move the index forward by 2 characters
            index += 2

# Output the final result
print(result)

# End

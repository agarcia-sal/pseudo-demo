# BEGIN

# Read a line of input and remove any extra spaces from the beginning and end
s = input().strip()  # INPUT string s FROM standard input and REMOVE whitespace

# Initialize an index to traverse the string and a variable to store the result
index = 0
result = ""

# Loop through the string until the end is reached
while index < len(s):  # WHILE index is less than the length of s

    # Check if the current character is a period (.)
    if s[index] == '.':  # IF character at index of s is '.'
        # If it's a period, append '0' to the result
        result += '0'  # APPEND '0' to result
        # Move to the next character
        index += 1  # INCREMENT index by 1

    # Otherwise, check the next character
    else:  # ELSE
        # Check if the next character is also a period (.)
        if index + 1 < len(s) and s[index + 1] == '.':  # IF character at index + 1 of s is '.'
            # If the next character is a period, append '1' to the result
            result += '1'  # APPEND '1' to the result
            # Move the index forward by 2 characters
            index += 2  # INCREMENT index by 2

        # Otherwise, it means we have a different character
        else:  # ELSE
            # Append '2' to the result
            result += '2'  # APPEND '2' to the result
            # Move the index forward by 2 characters
            index += 2  # INCREMENT index by 2

# END WHILE

# Output the final result
print(result)  # PRINT result

# END

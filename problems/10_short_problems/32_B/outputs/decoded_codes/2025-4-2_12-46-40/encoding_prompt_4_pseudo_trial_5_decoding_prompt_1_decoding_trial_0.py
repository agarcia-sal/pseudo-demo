BEGIN

    // Read input from standard input
    INPUT string s

    // Initialize index and result variable
    SET index to 0
    SET output to empty string

    // Process the input string
    WHILE index is less than the length of s DO
        IF s[index] equals '.' THEN
            // Current character is '.', map it to '0'
            APPEND '0' to output
            INCREMENT index by 1
        ELSE IF the next character s[index + 1] equals '.' THEN
            // Next character is also '.', map the current to '1'
            APPEND '1' to output
            INCREMENT index by 2
        ELSE
            // Neither of the two characters is '.', map it to '2'
            APPEND '2' to output
            INCREMENT index by 2
        END IF
    END WHILE

    // Display the result
    PRINT output

END


# Read input from standard input
s = input()

# Initialize index and result variable
index = 0
output = ""

# Process the input string
while index < len(s):
    if s[index] == '.':
        # Current character is '.', map it to '0'
        output += '0'
        index += 1
    elif index + 1 < len(s) and s[index + 1] == '.':
        # Next character is also '.', map the current to '1'
        output += '1'
        index += 2
    else:
        # Neither of the two characters is '.', map it to '2'
        output += '2'
        index += 2

# Display the result
print(output)

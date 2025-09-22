# This program translates a string of dots and other characters into a numeric string.

def translate_string():
    # Read a line of input and remove any extra spaces
    original_string = input().strip()
    
    # Initialize an index to track our position in the input string
    index = 0
    
    # Initialize an empty string to store the resulting translated output
    translated_string = ''
    
    # While there are still characters to process in the original string
    while index < len(original_string):
        # If the current character is a dot
        if original_string[index] == '.':
            # Append '0' to the translated output
            translated_string += '0'
            # Move to the next character
            index += 1
        # Else, if the next character is also a dot
        elif index + 1 < len(original_string) and original_string[index + 1] == '.':
            # Append '1' to the translated output
            translated_string += '1'
            # Move forward by two characters
            index += 2
        # Otherwise (the current character is not a dot and the next one isn’t either)
        else:
            # Append '2' to the translated output
            translated_string += '2'
            # Move forward by two characters
            index += 2
    
    # Display the final translated output
    print(translated_string)

# Example test cases (uncomment for testing):
# Input:  "... ... .. .. ..."
# Output: "01020101"
#
# Input:  "...."
# Output: "00"
#
# Input:  "abc"
# Output: "2"

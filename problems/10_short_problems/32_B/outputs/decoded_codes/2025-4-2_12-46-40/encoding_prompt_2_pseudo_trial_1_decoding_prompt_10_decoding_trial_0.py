def generate_digit_string():
    # Step 1: Read the input string and trim whitespace
    input_string = input().strip()

    # Step 2: Initialize index and result string
    index = 0
    result = ""

    # Step 3: Loop through the input string until the end
    while index < len(input_string):
        # Check if the current character is a dot
        if input_string[index] == '.':
            result += '0'  # Append '0' to result if current character is '.'
            index += 1     # Move to the next character
        else:
            # Check the next character if within the bounds of the string
            if index + 1 < len(input_string):
                if input_string[index + 1] == '.':
                    result += '1'  # Append '1' if the next character is '.'
                    index += 2     # Move forward by two characters
                else:
                    result += '2'  # Append '2' if the next character is not '.'
                    index += 2     # Move forward by two characters
            else:
                # If current character is not '.' and there's no next character
                result += '2'  # Append '2' for the last character
                index += 1     # Move to the next character

    # Step 5: Output the final result
    print(result)

# Call the function to execute the code
generate_digit_string()


Input: "....a..b.."
Output: "000211"

Input: ".a.b"
Output: "021"

Input: ".."
Output: "00"

Input: "abc"
Output: "222"

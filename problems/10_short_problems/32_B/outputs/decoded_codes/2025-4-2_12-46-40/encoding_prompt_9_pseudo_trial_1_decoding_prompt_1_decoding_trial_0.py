# Read Input
input_string = input()

# Initialize Variables
index = 0
result_string = ""

# Process Each Symbol
while index < len(input_string):
    if input_string[index] == '.':
        result_string += '0'
        index += 1  # Move to the next symbol
    else:
        if index + 1 < len(input_string):  # Ensure there is a next symbol
            if input_string[index + 1] == '.':
                result_string += '1'
                index += 2  # Skip to the next pair of symbols
            else:
                result_string += '2'
                index += 2  # Skip to the next pair of symbols
        else:
            index += 1  # In case there's an unmatched symbol at the end

# Output the Result
print(result_string)

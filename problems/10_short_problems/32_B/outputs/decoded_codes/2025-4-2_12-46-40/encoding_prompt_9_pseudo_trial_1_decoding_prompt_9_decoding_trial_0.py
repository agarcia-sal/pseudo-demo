# Read Input
input_string = input()

# Initialize Variables
index = 0
result_string = ""

# Process Each Symbol
while index < len(input_string):
    if input_string[index] == ".":
        result_string += "0"  # Append "0" for a single dot
        index += 1
    else:
        # Check the next symbol
        if index + 1 < len(input_string) and input_string[index + 1] == ".":
            result_string += "1"  # Append "1" for a pair of symbols (dot followed by dot)
            index += 2
        else:
            result_string += "2"  # Append "2" for a pair of symbols (dot and a non-dot or two non-dots)
            index += 2

# Output the Result
print(result_string)

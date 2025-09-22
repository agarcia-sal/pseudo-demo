# Start of the program

# Step 2: Accept Input
input_string = input().strip()  # Read input and remove extra spaces

# Step 3: Initialize Variables
index = 0  # Current position in input_string
result = ""  # String to build the final output

# Step 4: Process Input
while index < len(input_string):  # While there are still characters to process
    if input_string[index] == ".":  # Check if the current character is a dot
        result += "0"  # Append "0" to the result
        index += 1  # Move to the next position
    elif index + 1 < len(input_string) and input_string[index + 1] == ".":  # Check next character for a dot
        result += "1"  # Append "1" to the result
        index += 2  # Move ahead by two positions
    else:  # If current character is not a dot and next character is not a dot
        result += "2"  # Append "2" to the result
        index += 2  # Move ahead by two positions

# Step 5: Output the Result
print(result)  # Display the final result string

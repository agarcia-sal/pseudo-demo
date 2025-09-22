# Step 1: Read the input string and remove any extra spaces around it
input_string = input().strip()

# Step 2: Initialize variables
current_position = 0  # to keep track of our position in the input string
result = ''  # to accumulate the result of the processing

# Step 3: Process the input string based on the defined logic
while current_position < len(input_string):
    if input_string[current_position] == '.':
        result += '0'  # if current is a dot, append '0' to result
        current_position += 1  # move to the next character
    elif (current_position + 1 < len(input_string)) and (input_string[current_position + 1] == '.'):
        result += '1'  # if the next character is also a dot, append '1' to result
        current_position += 2  # move ahead by 2 positions
    else:
        result += '2'  # if it's neither a dot nor a pair of dots, append '2' to result
        current_position += 2  # move ahead by 2 positions

# Step 4: Output the result
print(result)  # print the final result string

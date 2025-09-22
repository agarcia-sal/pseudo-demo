# Step 1: Read Input
input_string = input()

# Step 2: Initialize Variables
index = 0
result = ""

# Step 3: Process Each Symbol
while index < len(input_string):
    if input_string[index] == ".":
        result += "0"
        index += 1
    else:
        if index + 1 < len(input_string) and input_string[index + 1] == ".":
            result += "1"
            index += 2
        else:
            result += "2"
            index += 2

# Step 4: Output the Result
print(result)

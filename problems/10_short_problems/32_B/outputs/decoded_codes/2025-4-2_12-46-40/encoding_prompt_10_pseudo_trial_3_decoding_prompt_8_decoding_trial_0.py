# Step 1: Read input and initialize variables
inputString = input().strip()
index = 0
answer = ""

# Step 2: Process each character in the input string
while index < len(inputString):
    if inputString[index] == '.':
        answer += '0'
        index += 1
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        answer += '1'
        index += 2
    else:
        answer += '2'
        index += 2

# Step 3: Output the result
print(answer)


def convert_input_to_output(inputString):
    inputString = inputString.strip()
    index = 0
    answer = ""

    while index < len(inputString):
        if inputString[index] == '.':
            answer += '0'
            index += 1
        elif index + 1 < len(inputString) and inputString[index + 1] == '.':
            answer += '1'
            index += 2
        else:
            answer += '2'
            index += 2
            
    return answer

# Step to read input and print output can remain the same
inputString = input()
print(convert_input_to_output(inputString))

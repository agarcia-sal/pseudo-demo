# Start Program

# Initialize Input
inputString = input().strip()

# Initialize Variables
index = 0
result = ""

# Process Input String Using a Loop
while index < len(inputString):
    # Check Current Character
    if inputString[index] == '.':
        result += '0'
        index += 1
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        result += '1'
        index += 2
    else:
        result += '2'
        index += 2

# Output Result
print(result)

# End Program


def translate_input(inputString):
    index = 0
    result = ""
    
    while index < len(inputString):
        if inputString[index] == '.':
            result += '0'
            index += 1
        elif index + 1 < len(inputString) and inputString[index + 1] == '.':
            result += '1'
            index += 2
        else:
            result += '2'
            index += 2
            
    return result

# Main Program
if __name__ == "__main__":
    inputString = input().strip()
    print(translate_input(inputString))

# Function to Compare Character Frequencies
def compareCharacterFrequencies():
    # Collect Input
    inputStrings = []
    for _ in range(2):  # Loop to collect two input strings
        inputString = input()  # Read input string
        inputString = inputString.replace(" ", "")  # Remove spaces
        inputStrings.append(inputString)  # Add to inputStrings
    
    string1 = inputStrings[0]  # Assign first string
    string2 = inputStrings[1]  # Assign second string

    # Count Character Frequencies
    frequencyDifference = []
    for char_code in range(65, 123):  # From 'A' (65) to 'z' (122)
        char = chr(char_code)  # Convert character code to character
        count1 = string1.count(char)  # Count occurrences in string1
        count2 = string2.count(char)  # Count occurrences in string2
        difference = count1 - count2  # Calculate difference
        frequencyDifference.append(difference)  # Add to frequencyDifference

    # Check Frequency Condition
    isValid = True  # Initialize validity check
    for value in frequencyDifference:  # Check each frequency difference
        if value < 0:  # If any difference is less than 0
            isValid = False  # Set isValid to false
            break  # Exit loop if condition is met

    # Output Result
    if isValid:  # If all conditions are met
        print("YES")
    else:
        print("NO")

# Call the function to execute the logic
compareCharacterFrequencies()

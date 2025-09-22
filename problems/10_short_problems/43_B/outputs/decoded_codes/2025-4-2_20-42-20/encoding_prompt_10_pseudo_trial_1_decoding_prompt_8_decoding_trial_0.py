def main():
    # Step 1: Accept two lines of input from the user
    firstLine = input()
    secondLine = input()

    # Step 2: Remove spaces from both lines
    cleanedFirstLine = remove_spaces(firstLine)
    cleanedSecondLine = remove_spaces(secondLine)

    # Step 3: Initialize frequency count for characters
    frequencyCounts = [0] * 58  # Assuming 'A' to 'z' includes 58 characters

    # Step 4: Calculate frequency differences
    for charValue in range(ord('A'), ord('z') + 1):
        count = cleanedFirstLine.count(chr(charValue)) - cleanedSecondLine.count(chr(charValue))
        frequencyCounts[charValue - ord('A')] = count

    # Step 5: Check for negative frequency counts
    isValid = True
    for count in frequencyCounts:
        if count < 0:
            isValid = False
            break  # Exit loop early if any count is negative

    # Step 6: Print result based on frequencies
    if isValid:
        print("YES")
    else:
        print("NO")

# Helper Function to Remove Spaces from String
def remove_spaces(inputString):
    result = ""
    for character in inputString:
        if character != ' ':
            result += character
    return result

# Run the main function
main()

def main():
    # Get two input strings from the user
    firstString = input()
    secondString = input()

    # Remove all spaces from the input strings
    firstStringWithoutSpaces = remove_spaces(firstString)
    secondStringWithoutSpaces = remove_spaces(secondString)

    # Initialize a list to hold frequency differences
    frequencyDifferences = []

    # Calculate frequency differences for each character from 'A' to 'z'
    for characterCode in range(ord('A'), ord('z') + 1):
        countInFirstString = count_occurrences(firstStringWithoutSpaces, characterCode)
        countInSecondString = count_occurrences(secondStringWithoutSpaces, characterCode)
        difference = countInFirstString - countInSecondString
        frequencyDifferences.append(difference)

    # Check if there are any negative frequency differences
    if all(diff >= 0 for diff in frequencyDifferences):
        print("YES")  # Indicates first string can be made to match second string
    else:
        print("NO")   # Indicates first string cannot be made to match second string

def remove_spaces(inputString):
    # Remove all spaces from the input string
    return inputString.replace(" ", "")

def count_occurrences(inputString, characterCode):
    # Return number of times the character corresponding to characterCode occurs in inputString
    character = chr(characterCode)  # Convert ASCII code to character
    return inputString.count(character)

# This allows the main function to run when the script is executed.
if __name__ == "__main__":
    main()

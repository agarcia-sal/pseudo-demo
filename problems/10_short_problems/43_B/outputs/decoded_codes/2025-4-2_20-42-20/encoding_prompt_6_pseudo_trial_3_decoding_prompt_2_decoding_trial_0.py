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
    return inputString.replace(" ", "")  # Return inputString with all spaces removed


def count_occurrences(inputString, characterCode):
    character = chr(characterCode)  # Get the character corresponding to characterCode
    return inputString.count(character)  # Return number of times character occurs in inputString


# Call the main function to execute the program
main()

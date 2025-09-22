def checkStringDifference():
    # Read two strings from user input
    firstInput = input()
    secondInput = input()
    
    # Create a list of characters from each input string, excluding spaces
    charactersFromFirstInput = [character for character in firstInput if character != ' ']
    charactersFromSecondInput = [character for character in secondInput if character != ' ']

    # Create a frequency list to count character occurrences (using a dictionary)
    frequencyDifferences = [0] * (123)  # ASCII range from 0 to 122 (using size 123 for simplicity)
    
    # Calculate the frequency of characters in the first and second input strings
    for character in charactersFromFirstInput:
        ascii_value = ord(character)  # Get ASCII value of the character
        frequencyDifferences[ascii_value] += 1  # Increment count

    for character in charactersFromSecondInput:
        ascii_value = ord(character)  # Get ASCII value of the character
        frequencyDifferences[ascii_value] -= 1  # Decrement count

    # Check if there are any negative differences
    negativeCount = sum(1 for count in frequencyDifferences if count < 0)

    # Output result based on whether all counts are non-negative
    if negativeCount == 0:
        print("YES")
    else:
        print("NO")

# Example usage: To check the function, uncomment the following line:
# checkStringDifference()

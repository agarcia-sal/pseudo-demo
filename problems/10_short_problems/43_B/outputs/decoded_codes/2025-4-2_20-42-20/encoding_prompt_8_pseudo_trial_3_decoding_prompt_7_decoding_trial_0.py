# Begin the program
def main():
    # Get input from the user, two separate strings
    firstInput = input()
    secondInput = input()

    # Remove spaces from both input strings
    firstStringCharacters = [char for char in firstInput if char != ' ']
    secondStringCharacters = [char for char in secondInput if char != ' ']

    # Initialize a list to store frequency differences
    frequencyDifferences = []

    # For each character in the range from 'A' to 'z'
    for characterCode in range(ord('A'), ord('z') + 1):
        # Convert character code to character
        currentCharacter = chr(characterCode)

        # Count occurrences of currentCharacter in firstStringCharacters
        countInFirstInput = firstStringCharacters.count(currentCharacter)

        # Count occurrences of currentCharacter in secondStringCharacters
        countInSecondInput = secondStringCharacters.count(currentCharacter)

        # Calculate the difference in counts and add to the list
        difference = countInFirstInput - countInSecondInput
        frequencyDifferences.append(difference)

    # Check if there are any negative differences
    negativeCount = sum(1 for diff in frequencyDifferences if diff < 0)

    # Output "YES" if there are no negative differences, otherwise "NO"
    if negativeCount == 0:
        print("YES")
    else:
        print("NO")

# Run the main function
if __name__ == "__main__":
    main()

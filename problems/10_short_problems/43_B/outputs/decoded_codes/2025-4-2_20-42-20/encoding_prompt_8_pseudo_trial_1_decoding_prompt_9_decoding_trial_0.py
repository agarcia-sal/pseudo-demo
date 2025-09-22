def main():
    # Get user input for both strings
    firstString = input()
    secondString = input()

    # Prepare strings by removing spaces
    cleanedFirstString = ''.join(c for c in firstString if c != ' ')
    cleanedSecondString = ''.join(c for c in secondString if c != ' ')

    # Initialize frequency list for 52 characters (A-Z, a-z)
    characterFrequency = [0] * 52

    # Function to get the index for the character
    def getIndex(char):
        if 'A' <= char <= 'Z':
            return ord(char) - ord('A')  # 0-25 for A-Z
        elif 'a' <= char <= 'z':
            return ord(char) - ord('a') + 26  # 26-51 for a-z
        return -1

    # Count characters in cleanedFirstString
    for char in cleanedFirstString:
        index = getIndex(char)
        if index != -1:
            characterFrequency[index] += 1

    # Count characters in cleanedSecondString
    for char in cleanedSecondString:
        index = getIndex(char)
        if index != -1:
            characterFrequency[index] -= 1

    # Check if the first string has sufficient characters
    isSufficient = True
    for count in characterFrequency:
        if count < 0:  # If any count is negative, we do not have enough characters
            isSufficient = False
            break

    # Output result
    if isSufficient:
        print("YES")
    else:
        print("NO")

# Call main function to execute the code
main()

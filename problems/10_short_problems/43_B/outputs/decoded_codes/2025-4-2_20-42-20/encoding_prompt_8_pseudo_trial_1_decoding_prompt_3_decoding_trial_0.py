def main():
    # Get user input for both strings
    firstString = input()
    secondString = input()

    # Prepare strings by removing spaces
    cleanedFirstString = firstString.replace(" ", "")
    cleanedSecondString = secondString.replace(" ", "")

    # Initialize a frequency list for counting characters (52 for A-Z and a-z)
    characterFrequency = [0] * 52

    # Count characters in cleanedFirstString
    for char in cleanedFirstString:
        if 'A' <= char <= 'Z':  # Uppercase letters
            index = ord(char) - ord('A')
        elif 'a' <= char <= 'z':  # Lowercase letters
            index = ord(char) - ord('a') + 26
        else:
            continue  # Ignore any other characters
        characterFrequency[index] += 1

    # Count characters in cleanedSecondString
    for char in cleanedSecondString:
        if 'A' <= char <= 'Z':  # Uppercase letters
            index = ord(char) - ord('A')
        elif 'a' <= char <= 'z':  # Lowercase letters
            index = ord(char) - ord('a') + 26
        else:
            continue  # Ignore any other characters
        characterFrequency[index] -= 1

    # Check character sufficiency
    isSufficient = True
    for count in characterFrequency:
        if count < 0:
            isSufficient = False
            break

    # Output the result
    if isSufficient:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()

def main():
    # Step 2: Get User Input
    firstString = input()  # Input for the first string
    secondString = input()  # Input for the second string

    # Step 3: Prepare Strings
    # Remove spaces from both strings
    cleanedFirstString = ''.join(firstString.split())
    cleanedSecondString = ''.join(secondString.split())

    # Step 4: Initialize Frequency List
    # List to hold frequency of characters (0 for 'A'-'Z' and 0 for 'a'-'z')
    characterFrequency = [0] * 52

    # Step 5: Count Characters
    # Count characters from the first string
    for char in cleanedFirstString:
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')  # Index for uppercase letters
        else:
            index = ord(char) - ord('a') + 26  # Index for lowercase letters
        characterFrequency[index] += 1  # Increment the frequency

    # Count characters from the second string
    for char in cleanedSecondString:
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')  # Index for uppercase letters
        else:
            index = ord(char) - ord('a') + 26  # Index for lowercase letters
        characterFrequency[index] -= 1  # Decrement the frequency

    # Step 6: Check Character Sufficiency
    isSufficient = True  # Assume first string is sufficient
    for count in characterFrequency:
        if count < 0:  # If any character frequency is negative
            isSufficient = False  # Not sufficient
            break  # No need to check further

    # Step 7: Output Result
    if isSufficient:
        print("YES")  # First string has enough characters
    else:
        print("NO")  # Not enough characters

# Call the main function to execute the program
main()

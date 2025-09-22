def main():
    # Get User Input
    firstString = input()
    secondString = input()
    
    # Prepare Strings
    cleanedFirstString = ''.join(c for c in firstString if c != ' ')
    cleanedSecondString = ''.join(c for c in secondString if c != ' ')
    
    # Initialize Frequency List
    characterFrequency = [0] * 52  # 26 uppercase + 26 lowercase
    
    # Count Characters
    for c in cleanedFirstString:
        if 'A' <= c <= 'Z':
            index = ord(c) - ord('A')  # Map 'A'-'Z' to 0-25
            characterFrequency[index] += 1
        elif 'a' <= c <= 'z':
            index = ord(c) - ord('a') + 26  # Map 'a'-'z' to 26-51
            characterFrequency[index] += 1
    
    for c in cleanedSecondString:
        if 'A' <= c <= 'Z':
            index = ord(c) - ord('A')  # Map 'A'-'Z' to 0-25
            characterFrequency[index] -= 1
        elif 'a' <= c <= 'z':
            index = ord(c) - ord('a') + 26  # Map 'a'-'z' to 26-51
            characterFrequency[index] -= 1

    # Check Character Sufficiency
    isSufficient = True
    for count in characterFrequency:
        if count < 0:
            isSufficient = False
            break
    
    # Output Result
    if isSufficient:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()

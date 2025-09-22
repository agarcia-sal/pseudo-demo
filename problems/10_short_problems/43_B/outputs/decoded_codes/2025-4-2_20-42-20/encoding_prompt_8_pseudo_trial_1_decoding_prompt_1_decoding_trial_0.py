def main():
    # Get User Input
    firstString = input()
    secondString = input()
    
    # Prepare Strings
    cleanedFirstString = ''.join(firstString.split())
    cleanedSecondString = ''.join(secondString.split())
    
    # Initialize Frequency List
    characterFrequency = [0] * 52  # 26 uppercase and 26 lowercase letters

    # Count Characters
    for char in cleanedFirstString:
        if 'A' <= char <= 'Z':
            characterFrequency[ord(char) - ord('A')] += 1
        elif 'a' <= char <= 'z':
            characterFrequency[ord(char) - ord('a') + 26] += 1
            
    for char in cleanedSecondString:
        if 'A' <= char <= 'Z':
            characterFrequency[ord(char) - ord('A')] -= 1
        elif 'a' <= char <= 'z':
            characterFrequency[ord(char) - ord('a') + 26] -= 1

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

# Call the main function to execute
main()

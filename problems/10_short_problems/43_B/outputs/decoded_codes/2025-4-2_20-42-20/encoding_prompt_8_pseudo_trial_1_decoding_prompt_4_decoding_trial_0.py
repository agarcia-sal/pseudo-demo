def main():
    # Step 2: Get User Input
    firstString = input()
    secondString = input()
    
    # Step 3: Prepare Strings
    cleanedFirstString = ''.join(firstString.split())
    cleanedSecondString = ''.join(secondString.split())
    
    # Step 4: Initialize Frequency List
    characterFrequency = [0] * 52  # 26 for 'A'-'Z' and 26 for 'a'-'z'
    
    # Step 5: Count Characters
    for char in cleanedFirstString:
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')  # Uppercase index
        elif 'a' <= char <= 'z':
            index = ord(char) - ord('a') + 26  # Lowercase index
        else:
            continue  # Ignore characters not in A-z
        characterFrequency[index] += 1

    for char in cleanedSecondString:
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')  # Uppercase index
        elif 'a' <= char <= 'z':
            index = ord(char) - ord('a') + 26  # Lowercase index
        else:
            continue  # Ignore characters not in A-z
        characterFrequency[index] -= 1
    
    # Step 6: Check Character Sufficiency
    isSufficient = True
    for count in characterFrequency:
        if count < 0:
            isSufficient = False
            break
    
    # Step 7: Output Result
    if isSufficient:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()

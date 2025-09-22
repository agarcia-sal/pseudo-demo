def main():
    # Get Input Strings
    stringOne = [char for char in input() if char != ' ']
    stringTwo = [char for char in input() if char != ' ']

    # Initialize Frequency List
    characterFrequency = [0] * (ord('z') - ord('A') + 1) # Covers characters 'A' to 'z'

    # Count Character Frequencies
    for char in stringOne:
        characterFrequency[ord(char) - ord('A')] += 1
        
    for char in stringTwo:
        characterFrequency[ord(char) - ord('A')] -= 1

    # Check for Sufficient Characters
    if all(freq >= 0 for freq in characterFrequency):
        print("YES")
    else:
        print("NO")

# Call the main function
main()

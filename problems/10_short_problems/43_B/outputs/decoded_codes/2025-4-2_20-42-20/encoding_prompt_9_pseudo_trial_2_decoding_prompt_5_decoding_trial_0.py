# Function to check if secondString can be constructed from firstString
def can_construct_string():
    # Input the two strings from the user
    first_string = input()
    second_string = input()
    
    # Remove spaces from both strings
    first_string = first_string.replace(" ", "")
    second_string = second_string.replace(" ", "")
    
    # Initialize frequency counts for characters A to z
    character_differences = [0] * (ord('z') - ord('A') + 1)
    
    # Count frequency of each character in firstString
    for char in first_string:
        index = ord(char) - ord('A')
        character_differences[index] += 1
    
    # Count frequency of each character in secondString
    for char in second_string:
        index = ord(char) - ord('A')
        character_differences[index] -= 1
    
    # Check for negative counts in characterDifferences
    for difference in character_differences:
        if difference < 0:
            print("NO")
            return
    
    # If no negative counts are found, print YES
    print("YES")

# It is encouraged to call the function here to test it after defining
# can_construct_string()

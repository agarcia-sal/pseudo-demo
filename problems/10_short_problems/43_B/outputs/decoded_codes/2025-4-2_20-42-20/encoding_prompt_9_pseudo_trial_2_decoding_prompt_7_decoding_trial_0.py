# Function to check if second string can be constructed from first string
def can_construct_string():
    # Step 1: Input Strings
    firstString = input()
    secondString = input()

    # Step 2: Process Input: Remove spaces
    firstString = firstString.replace(" ", "")
    secondString = secondString.replace(" ", "")

    # Step 3: Initialize Frequency Count
    # Create a list to hold the frequency count of characters
    # Using a dictionary for more flexibility
    characterDifferences = {}
    
    # Count occurrences of each character in firstString
    for char in firstString:
        if char in characterDifferences:
            characterDifferences[char] += 1
        else:
            characterDifferences[char] = 1

    # Subtract occurrences of each character in secondString from the first
    for char in secondString:
        if char in characterDifferences:
            characterDifferences[char] -= 1
        else:
            # If the character in secondString doesn’t exist in firstString
            characterDifferences[char] = -1

    # Step 4: Check Feasibility
    # Count negative values (indicating insufficient characters)
    negative_count = sum(1 for count in characterDifferences.values() if count < 0)

    # Step 5: Output the Result
    if negative_count > 0:
        print("NO")
    else:
        print("YES")

# Call the function to run the program
can_construct_string()

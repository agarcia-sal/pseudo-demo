def can_transform_string():
    # Retrieve Input
    firstString = input()
    secondString = input()

    # Preprocess Input
    cleanedStrings = [
        firstString.replace(" ", ""),  # Remove spaces from firstString
        secondString.replace(" ", "")   # Remove spaces from secondString
    ]
    s1, s2 = cleanedStrings  # Cleaned strings assigned to s1 and s2

    # Count Character Frequencies
    frequencyDifference = []
    for char in range(ord('A'), ord('z') + 1):
        # Count occurrences of the character in both strings
        count1 = s1.count(chr(char))
        count2 = s2.count(chr(char))
        
        # Calculate difference and append to frequencyDifference
        frequencyDifference.append(count1 - count2)

    # Check Character Count Requirements
    insufficient_count = sum(1 for diff in frequencyDifference if diff < 0)

    # Provide Output
    if insufficient_count == 0:
        print("YES")  # Transformation is possible
    else:
        print("NO")   # Transformation is not possible

# Run the function
can_transform_string()

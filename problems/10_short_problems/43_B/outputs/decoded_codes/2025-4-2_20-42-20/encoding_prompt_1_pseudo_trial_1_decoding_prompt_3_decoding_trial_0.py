def compare_character_frequencies():
    # Step 1: Input two strings from the user
    firstString = input()
    secondString = input()
    
    # Step 2: Process Input by removing spaces
    cleanedFirst = firstString.replace(" ", "")
    cleanedSecond = secondString.replace(" ", "")
    
    # Step 3: Initialize the Frequency Difference List
    frequencyDifferences = []
    
    # Step 4: Count Character Frequencies
    for char in range(ord('A'), ord('z') + 1):
        # Convert ASCII value to character
        character = chr(char)
        
        # Count occurrences in both cleaned strings
        countInFirst = cleanedFirst.count(character)
        countInSecond = cleanedSecond.count(character)
        
        # Calculate the frequency difference and append to the list
        frequencyDifferences.append(countInFirst - countInSecond)
    
    # Step 5: Check Frequency Differences
    negative_count = sum(1 for difference in frequencyDifferences if difference < 0)
    
    # Step 6: Output Result
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute
compare_character_frequencies()

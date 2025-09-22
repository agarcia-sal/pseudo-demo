def compare_strings():
    # Initialize variables to hold the input strings without spaces
    first_input = input().replace(" ", "")
    second_input = input().replace(" ", "")
    
    # Create a list to hold frequency differences
    character_frequency_difference = [0] * 128  # Assuming ASCII range

    # Count character frequencies
    for char in first_input:
        character_frequency_difference[ord(char)] += 1  # Increment count for first_input

    for char in second_input:
        character_frequency_difference[ord(char)] -= 1  # Decrement count for second_input

    # Evaluate results by checking the frequency difference
    for count in character_frequency_difference:
        if count < 0:  # If any character in second_input has a higher count
            print("NO")
            return

    # If we haven't found any negative counts, print YES
    print("YES")

# Call the function to execute the comparison
compare_strings()

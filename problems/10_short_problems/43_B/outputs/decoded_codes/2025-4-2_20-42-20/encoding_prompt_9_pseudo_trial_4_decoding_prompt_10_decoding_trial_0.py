def can_form_string():
    # Step 1: Receive Input
    first_string = input()
    second_string = input()

    # Step 2: Process Input
    cleaned_first_string = first_string.replace(" ", "")
    cleaned_second_string = second_string.replace(" ", "")

    # Step 3: Initialize Frequency Count
    # There are 256 possible characters (from ASCII range)
    character_frequencies = [0] * 256  

    # Step 4: Count Character Frequencies
    for character in cleaned_first_string:
        character_frequencies[ord(character)] += 1  # Increment count for character

    for character in cleaned_second_string:
        character_frequencies[ord(character)] -= 1  # Decrement count for character

    # Step 5: Evaluate Frequencies
    has_shortages = 'NO'
    
    for count in character_frequencies:
        if count < 0:
            has_shortages = 'YES'  # A shortage was found
            break
            
    # Step 6: Output Result
    if has_shortages == 'NO':
        print("YES")
    else:
        print("NO")

# Call the function to execute
can_form_string()

def can_construct_string():
    # Step 1: Input Strings
    first_string = input()
    second_string = input()
    
    # Step 2: Process Input
    first_string = first_string.replace(" ", "")
    second_string = second_string.replace(" ", "")
    
    # Step 3: Initialize Frequency Count
    # Using a dictionary to count character occurrences
    character_count = {}
    
    for char in first_string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    
    # Check feasibility
    for char in second_string:
        if char in character_count:
            character_count[char] -= 1
        else:
            print("NO")
            return
        
        # Early exit if count drops below zero
        if character_count[char] < 0:
            print("NO")
            return

    # Step 5: Output the Result
    print("YES")

# Call the function to execute
can_construct_string()

def can_construct_string():
    # Step 1: Input Strings
    first_string = input()
    second_string = input()
    
    # Step 2: Process Input
    first_string = first_string.replace(" ", "")
    second_string = second_string.replace(" ", "")
    
    # Step 3: Initialize Frequency Count
    character_differences = [0] * 256  # Assuming ASCII characters
    
    # Count characters in firstString
    for char in first_string:
        character_differences[ord(char)] += 1
    
    # Count characters in secondString
    for char in second_string:
        character_differences[ord(char)] -= 1
    
    # Step 4: Check Feasibility
    negative_count = sum(1 for count in character_differences if count < 0)
    
    # Step 5: Output the Result
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute the program
can_construct_string()


   Hello World
   Hold
   

   YES
   

   Python Programming
   Grape
   

   NO
   
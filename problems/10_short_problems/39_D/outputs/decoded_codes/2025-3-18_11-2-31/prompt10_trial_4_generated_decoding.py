def do_main():
    # Step 1: Read input from user
    input_1 = input()  # First set of numbers
    input_2 = input()  # Second set of numbers
    
    # Step 2: Split the input strings into lists
    list_1 = input_1.split()  # Convert string input to a list of substrings
    list_2 = input_2.split()  # Convert string input to a list of substrings
    
    # Step 3: Initialize a counter for differences
    difference_count = 0 
    
    # Step 4: Compare elements in both lists
    for i in range(3):  # We know there are always three elements
        # Convert string elements to integers
        num_1 = int(list_1[i])
        num_2 = int(list_2[i])
        
        # Check if the numbers are different
        if num_1 != num_2:
            difference_count += 1 
    
    # Step 5: Output result based on differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 6: Program entry point
if __name__ == "__main__":
    do_main()


        1 2 3
        1 2 3
        

        1 2 3
        1 2 4
        

        1 2 3
        4 5 6
        
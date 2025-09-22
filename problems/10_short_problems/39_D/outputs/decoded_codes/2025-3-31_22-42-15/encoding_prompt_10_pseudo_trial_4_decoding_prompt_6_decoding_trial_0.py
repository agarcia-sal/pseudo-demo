def do_main():
    # Step 1: Read input values
    input_t1 = input()
    input_t2 = input()
    
    # Step 2: Split inputs into lists of strings
    list_t1 = input_t1.split()
    list_t2 = input_t2.split()
    
    # Step 3: Initialize a result counter
    result_count = 0
    
    # Step 4: Loop to compare elements in both lists
    for index in range(3):  # Looping for three elements as assumed
        # Convert string to integer for comparison
        value_a = int(list_t1[index])
        value_b = int(list_t2[index])
        
        # Step 5: Check if the values are different
        if value_a != value_b:
            result_count += 1  # Increment the count of differences
    
    # Step 6: Determine if the result count is less than 3
    if result_count < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the main function
do_main()

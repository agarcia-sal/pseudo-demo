def do_main():
    # Step 1: Gather Input
    input1 = input()  # Get first input from the user
    input2 = input()  # Get second input from the user

    # Step 2: Split Inputs into Lists
    list1 = input1.split()  # Split first input into a list using whitespace
    list2 = input2.split()  # Split second input into a list using whitespace

    # Step 3: Initialize a Result Counter
    result_counter = 0  # Counter for differing elements

    # Step 4: Compare Elements of Both Lists
    for index in range(3):  # Loop through the first three elements
        # Convert current elements to integers
        value_from_list1 = int(list1[index])  # Convert element from list1 to integer
        value_from_list2 = int(list2[index])  # Convert element from list2 to integer
        
        # Step 5: Check if the values are different
        if value_from_list1 != value_from_list2:  # Check for inequality
            result_counter += 1  # Increment the counter if values are different

    # Step 6: Determine the Result
    if result_counter < 3:  # If less than 3 differences
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Step 7: Execute the Main Function
do_main()  # Call the main function to run the program

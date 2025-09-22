def main():
    # Step 1: Prompt the user for input
    user_input1 = input()
    user_input2 = input()

    # Step 2: Split the input strings into individual components
    value_list1 = user_input1.split()
    value_list2 = user_input2.split()

    # Step 3: Initialize a counter for differences
    difference_counter = 0

    # Step 4: Compare the corresponding values from both lists
    for index in range(3):  # Only comparing the first three values (0 to 2)
        value_a = int(value_list1[index])  # Convert value from list 1 to integer
        value_b = int(value_list2[index])  # Convert value from list 2 to integer

        # Step 5: Check for differences
        if value_a != value_b:
            difference_counter += 1  # Increment the counter if values are different

    # Step 6: Evaluate the total differences
    if difference_counter < 3:
        print("YES")  # Output if differences are less than 3
    else:
        print("NO")   # Output if differences are 3 or more

# Step 7: End the program by calling the main function
if __name__ == "__main__":
    main()

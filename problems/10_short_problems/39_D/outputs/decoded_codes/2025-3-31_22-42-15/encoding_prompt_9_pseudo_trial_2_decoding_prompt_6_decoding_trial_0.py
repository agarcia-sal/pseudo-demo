def do_main():
    # Step 2: Receive Input
    first_set = input()  # Get first set of numbers from user
    second_set = input()  # Get second set of numbers from user

    # Step 3: Split the Input into lists
    list_first = first_set.split()  # Convert input string to list of numbers
    list_second = second_set.split()  # Convert input string to list of numbers

    # Step 4: Initialize Difference Counter
    difference_count = 0  # Set counter to track differences

    # Step 5: Compare the Numbers
    for index in range(3):  # Loop through the first three positions
        # Convert string to integer
        number_from_first = int(list_first[index])
        number_from_second = int(list_second[index])
        
        # Check if the numbers differ
        if number_from_first != number_from_second:
            difference_count += 1  # Increment difference count if they are not equal

    # Step 6: Check Differences
    if difference_count < 3:
        print("YES")  # Output for fewer than three differences
    else:
        print("NO")  # Output if three or more differences

# Step 7: Execute the Function
if __name__ == "__main__":
    do_main()

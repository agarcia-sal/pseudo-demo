def main():
    # Step 1: Receive input for the first set of integers
    first_set = input()

    # Step 2: Receive input for the second set of integers
    second_set = input()

    # Step 3: Split the input into individual integers
    first_set_list = first_set.split()
    second_set_list = second_set.split()

    # Step 4: Initialize a counter for differences
    difference_count = 0

    # Step 5: Compare corresponding integers in both sets
    for index in range(3):
        # Convert the current string values to integers
        first_value = int(first_set_list[index])
        second_value = int(second_set_list[index])
        
        # Step 6: Check if the integers are different
        if first_value != second_value:
            difference_count += 1

    # Step 7: Determine if the two sets are considered similar
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 8: Execute the main function when the script runs
if __name__ == "__main__":
    main()

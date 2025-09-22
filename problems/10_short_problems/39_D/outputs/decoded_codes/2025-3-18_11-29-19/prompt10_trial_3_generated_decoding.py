def do_main():
    # Step 1: Get input from the user
    user_input_1 = input()
    user_input_2 = input()

    # Step 2: Split the input strings into lists of strings
    list_1 = user_input_1.split()
    list_2 = user_input_2.split()

    # Step 3: Initialize a variable to count differences
    difference_count = 0 

    # Step 4: Loop through the first three elements of both lists
    for index in range(3):
        # Step 5: Convert elements to integers
        value_1 = int(list_1[index])
        value_2 = int(list_2[index])

        # Step 6: Check for differences
        if value_1 != value_2:
            # Increment the count if they are different
            difference_count += 1 

    # Step 7: Determine output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution block
if __name__ == "__main__":
    do_main()

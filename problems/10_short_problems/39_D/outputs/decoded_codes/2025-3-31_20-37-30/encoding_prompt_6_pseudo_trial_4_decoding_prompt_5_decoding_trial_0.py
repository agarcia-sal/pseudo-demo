def main():
    # Step 1: Get two lines of input from the user
    first_string = input()
    second_string = input()

    # Step 2: Split the input strings into lists of numbers
    first_list = first_string.split()
    second_list = second_string.split()

    # Step 3: Initialize a counter to track differences
    difference_count = 0 

    # Step 4: Compare the numbers in each list
    for index in range(3):  # Assuming there are at least 3 elements
        first_number = int(first_list[index])
        second_number = int(second_list[index])
        
        # Step 5: Check if the numbers are different
        if first_number != second_number:
            difference_count += 1 

    # Step 6: Determine if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program by calling the main function
main()

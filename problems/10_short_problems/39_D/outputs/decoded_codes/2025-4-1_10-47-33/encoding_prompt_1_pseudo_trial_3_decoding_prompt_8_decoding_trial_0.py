def main():
    # Step 1: Read two lines of input from the user
    first_input = input()
    second_input = input()
    
    # Step 2: Split the input strings into lists of substrings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Step 3: Initialize a counter for differences
    difference_count = 0 

    # Step 4: Compare elements from both lists
    for index in range(3):
        # Convert the current elements to integers for comparison
        first_value = int(first_list[index])
        second_value = int(second_list[index])

        # Count how many values are different
        if first_value != second_value:
            difference_count += 1
    
    # Step 5: Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Invoke the main function
main()


def main(num_elements=3):
    # Read input, convert to lists, and initialize counter as before...
    # The loop from 0 to num_elements instead of hardcoding 3

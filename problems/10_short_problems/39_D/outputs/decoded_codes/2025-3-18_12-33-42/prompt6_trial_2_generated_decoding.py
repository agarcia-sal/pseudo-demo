def main():
    # Read two lines of input
    first_string = input()
    second_string = input()
    
    # Split each input string into a list of strings
    first_list = first_string.split()
    second_list = second_string.split()

    # Initialize a counter for different elements
    difference_count = 0

    # Loop through the first three elements in both lists
    for index in range(3):
        # Convert the current elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the elements are different
        if first_value != second_value:
            # Increment the counter of different elements
            difference_count += 1

    # Check if the count of different elements is less than 3
    if difference_count < 3:
        print("YES")  # Output YES if fewer than 3 elements are different
    else:
        print("NO")   # Output NO if 3 or more elements are different

# Entry point of the program
main()

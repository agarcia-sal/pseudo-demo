def main():
    # Gather inputs from the user
    first_input = input()
    second_input = input()

    # Split the input strings into lists of values
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a difference counter
    difference_count = 0 

    # Loop through the first three values of both lists
    for index in range(3):
        # Convert the current values from both lists to integers for comparison
        first_value = int(first_list[index])
        second_value = int(second_list[index])

        # Check if the values are different
        if first_value != second_value:
            difference_count += 1 
    
    # Check the number of differences
    if difference_count < 3:
        print("YES")  # They differ in fewer than three positions
    else:
        print("NO")   # They differ in three or more positions

# Start the program
main()

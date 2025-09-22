def main():
    # Read input values
    first_input = input()
    second_input = input()

    # Split the input strings into separate integer components
    first_list = list(map(int, first_input.split()))
    second_list = list(map(int, second_input.split()))

    # Initialize a counter for differences
    difference_count = 0 

    # Loop through the three integers
    for index in range(3):
        first_value = first_list[index]
        second_value = second_list[index]
        
        # Check if the values are different
        if first_value != second_value:
            difference_count += 1 

    # Determine if the number of differences is less than three
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program
main()

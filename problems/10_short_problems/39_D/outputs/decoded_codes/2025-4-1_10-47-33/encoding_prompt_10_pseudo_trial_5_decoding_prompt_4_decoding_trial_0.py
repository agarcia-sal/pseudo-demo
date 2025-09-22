def do_main():
    # Initialize the result counter
    result_counter = 0

    # Prompt the user for input
    print("Please enter the first line of numbers:")
    first_line = input()
    print("Please enter the second line of numbers:")
    second_line = input()

    # Split the input lines into lists of strings
    numbers_first_line = first_line.split()
    numbers_second_line = second_line.split()

    # Loop through the numbers and compare them
    for index in range(3):
        # Convert the strings to integers
        number_a = int(numbers_first_line[index])
        number_b = int(numbers_second_line[index])
        
        # Increment the result counter if the numbers are not equal
        if number_a != number_b:
            result_counter += 1

    # Determine the output based on the count of unequal numbers
    if result_counter < 3:
        print("YES")
    else:
        print("NO")

# Check if the script is executed as the main program
if __name__ == "__main__":
    do_main()

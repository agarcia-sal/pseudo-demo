def do_main():
    # Declare variables to hold the input strings
    first_line = ''
    second_line = ''
    result = 0

    # Read the first line of numbers from the user
    print("Please enter the first line of numbers:")
    first_line = input()
    
    # Read the second line of numbers from the user
    print("Please enter the second line of numbers:")
    second_line = input()

    # Split the input strings into lists of strings
    list_first_numbers = first_line.split()
    list_second_numbers = second_line.split()

    # Iterate through the lists and compare the numbers
    for index in range(3):  # since we expect exactly 3 numbers
        # Convert the strings to integers
        first_number = int(list_first_numbers[index])
        second_number = int(list_second_numbers[index])
        
        # Increment result if the numbers are not equal
        if first_number != second_number:
            result += 1

    # Output YES if less than 3 numbers are different, otherwise NO
    if result < 3:
        print("YES")
    else:
        print("NO")

# Check if the script is executed as the main program
if __name__ == "__main__":
    do_main()

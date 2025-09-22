def main():
    # Read two strings of input
    input_string1 = input()
    input_string2 = input()

    # Split the input strings into lists of words
    words_list1 = input_string1.split()
    words_list2 = input_string2.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the corresponding elements to integers
        number1 = int(words_list1[index])
        number2 = int(words_list2[index])

        # If the numbers are not the same, increment the difference counter
        if number1 != number2:
            difference_count += 1 

    # Check if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution block
if __name__ == "__main__":
    main()

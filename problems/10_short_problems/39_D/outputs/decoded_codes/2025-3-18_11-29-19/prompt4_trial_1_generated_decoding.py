def main():
    # Read two lines of input from the user
    first_line = input()
    second_line = input()
    
    # Split the input lines into lists of strings
    first_list = first_line.split()
    second_list = second_line.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the string elements to integers
        number_from_first_list = int(first_list[index])
        number_from_second_list = int(second_list[index])
        
        # Check if the two numbers are different
        if number_from_first_list != number_from_second_list:
            difference_count += 1  # Increment if the numbers are different
    
    # Output "YES" if less than 3 differences are found, otherwise output "NO"
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execution starts here
main()

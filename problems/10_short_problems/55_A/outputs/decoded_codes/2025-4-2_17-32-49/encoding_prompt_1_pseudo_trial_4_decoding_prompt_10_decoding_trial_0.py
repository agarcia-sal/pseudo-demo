def main():
    # Read an integer input that represents the size of the list
    size_of_list = int(input())
    
    # Create a boolean list initialized to True, indicating all elements are active
    boolean_list = [True] * size_of_list

    # Initialize index variables
    index_to_check = 0
    increment_value = 1

    # Loop until the increment value exceeds 500,000
    while increment_value <= 500_000:
        # If the current position in the boolean list is still active (True), deactivate it
        if boolean_list[index_to_check]:
            boolean_list[index_to_check] = False
        
        # Move to the next increment value
        increment_value += 1
        
        # Update the index to check, wrapping around if it exceeds the size of the list
        index_to_check = (index_to_check + increment_value) % size_of_list

    # Create a new list containing only the active elements (True) from the boolean list
    active_elements = [elem for elem in boolean_list if elem]

    # Check if there are any active elements left
    if len(active_elements) == 0:
        print('YES')  # Indicates that all elements have been deactivated
    else:
        print('NO')   # Indicates that some elements remain active

if __name__ == "__main__":
    main()

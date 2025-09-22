# Function to determine if all values in the list are changed to False
def check_status_list():
    # Step 2: Receive Input
    n = int(input())  # Read the size of the list

    # Step 3: Initialize List
    status_list = [True] * n  # Create a boolean list with n elements initialized to True

    # Step 4: Initialize Variables
    current_index = 0
    increment = 1

    # Step 5: Process List
    while increment <= 500000:
        # Check if the current index in status_list is True
        if status_list[current_index]:
            status_list[current_index] = False  # Change to False if it's True
        increment += 1  # Increase increment by 1
        # Update current_index with wrapping around using modulus
        current_index = (current_index + increment) % n

    # Step 6: Check Remaining Values
    remaining_true = [value for value in status_list if value]  # List of remaining True values

    # Step 7: Generate Output
    if not remaining_true:  # If remaining_true is empty
        print("YES")
    else:
        print("NO")

# Call the function
check_status_list()

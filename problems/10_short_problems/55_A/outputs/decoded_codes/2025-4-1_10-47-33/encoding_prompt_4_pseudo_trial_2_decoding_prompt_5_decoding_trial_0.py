# Read an integer input representing the number of elements
n = int(input())

# Create a list 'state' initialized with 'True' values to track the state
state = [True] * n

# Initialize counters
j = 0  # Index for the list
i = 1  # Counter for iterations

# Loop while i is less than or equal to 500000
while i <= 500000:
    # If the current index j in list state is True
    if state[j]:
        # Set that index to False
        state[j] = False

    # Increment i by 1
    i += 1
    
    # Update index j with wrapping around using modulus operator
    j = (j + i) % n

# Create a list 'truth_values' containing all True values from list 'state'
truth_values = [value for value in state if value]

# Check if the list 'truth_values' is empty
if len(truth_values) == 0:
    print('YES')  # Output if there are no True values
else:
    print('NO')   # Output if there are any True values

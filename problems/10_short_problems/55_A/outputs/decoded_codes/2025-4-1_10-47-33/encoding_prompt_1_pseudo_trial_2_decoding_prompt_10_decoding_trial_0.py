def process_active_elements():
    # Step 1: Initialize Input
    n = int(input())

    # Step 2: Create a Boolean List
    is_active = [True] * n

    # Step 3: Set Up Variables
    index = 0
    counter = 1

    # Step 4: Iterate While Counter is Less Than or Equal To 500000
    while counter <= 500000:
        if is_active[index]:
            is_active[index] = False
        counter += 1
        index = (index + counter) % n  # Wrap around using modulo

    # Step 5: Filter Active Elements
    active_elements = [element for element in is_active if element]

    # Step 6: Check Active Elements
    if len(active_elements) == 0:
        print("YES")
    else:
        print("NO")

# Example invocation (uncomment to run):
# process_active_elements()

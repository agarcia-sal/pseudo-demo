# Step 1: Start Program

# Step 2: Read Input
input_string = input().strip()  # Read a string input and remove leading/trailing whitespace

# Step 3: Normalize Path
def normalize_path(path):
    # Step 3a: Replace any sequences of forward slashes at the beginning of the path
    if path.startswith('/'):
        path = '/' + path.lstrip('/')
    
    # Step 3b: Normalize the path by replacing multiple forward slashes with a single one
    normalized_path = []
    parts = path.split('/')
    for part in parts:
        if part:  # Only add non-empty parts
            normalized_path.append(part)
    
    return '/' + '/'.join(normalized_path)  # Join with single slashes

# Call the normalize_path function
normalized_file_path = normalize_path(input_string)

# Step 4: Output Result
print(normalized_file_path)  # Display the normalized file path

# Step 5: End of Program

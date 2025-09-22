# Start Program

# Step 1: Receive Input
input_path = input()  # Get the input path from the user

# Step 2: Normalize Input Path
# Split the path into components, remove unnecessary empty components
path_components = input_path.split('/')  # Split the input on forward slashes
normalized_components = [component for component in path_components if component]  # Eliminate empty components

# Step 3: Format Path
# Join components back into a path
normalized_path = '/'.join(normalized_components)  # Join components with a single forward slash
# Ensure the path starts with a single forward slash
if normalized_path:  # Check if the normalized path is not empty
    formatted_path = '/' + normalized_path  # Prepend a single forward slash
else:
    formatted_path = '/'  # If the normalized path was empty, just set to root

# Step 4: Display Result
print(formatted_path)  # Output the formatted path to the user

# End Program

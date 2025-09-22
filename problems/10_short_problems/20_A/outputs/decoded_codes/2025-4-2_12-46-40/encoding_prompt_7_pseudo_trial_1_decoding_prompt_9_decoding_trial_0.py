def normalize(input_path):
    # Normalize the file path by resolving '..' and '.' references
    # Here we can use the os.path.normpath to achieve that
    import os
    normalized_version = os.path.normpath(input_path)
    return normalized_version

def normalize_and_print_path():
    # Read input from standard input and remove any leading/trailing whitespace
    input_path = input().strip()

    # Normalize the file path to remove unnecessary components
    normalized_path = normalize(input_path)

    # Replace any leading slashes with a single slash
    # To achieve this, we will use lstrip to remove multiple leading slashes
    final_path = normalized_path.lstrip('/')

    # Output the final formatted path
    print('/' + final_path)

# The function can be called to execute the normalization process
# Uncomment the line below to run the function when this script is executed
# normalize_and_print_path()

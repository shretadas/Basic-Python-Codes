#Install an external module and use it to perform an operation of your interest
import os

def list_files_and_directories():
    # Get the current working directory
    current_directory = os.getcwd()
    
    # List all files and directories in the current directory
    items = os.listdir(current_directory)
    
    print("Files and directories in '", current_directory, "':")
    for item in items:
        print(item)

# Call the function
list_files_and_directories()

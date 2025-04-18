def process_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            data = infile.read()
        
        lines = data.split('\n')
        words = data.split()
        characters = len(data)

        with open(output_file, 'w') as outfile:
            outfile.write(f"Lines: {len(lines)}\n")
            outfile.write(f"Words: {len(words)}\n")
            outfile.write(f"Characters: {characters}\n")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the input and output file names
input_file = r'C:\Users\dassh\Downloads\poems.txt'
output_file = r'C:\Users\dassh\Downloads\poem.txt'

# Call the function with the specified file names
process_file(input_file, output_file)

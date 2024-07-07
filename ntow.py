import inflect

def integer_to_words(num):
    p = inflect.engine()
    return p.number_to_words(num)

def main():
    try:
        file_name = "input_file.txt"  # Replace with your file name

        # Read the integer from the file
        with open(file_name, "r") as file:
            integer_str = file.readline().strip()
            num = int(integer_str)

        # Convert the integer to words
        words = integer_to_words(num)

        # Write the result back to the file
        with open(file_name, "a") as file:
            file.write(words)

        print("Conversion successful!")

    except FileNotFoundError:
        print("File not found. Please check the file name.")
    except ValueError:
        print("Invalid input in the file. Please provide a valid integer.")

if __name__ == "__main__":
    main()
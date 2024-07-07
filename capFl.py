def capitalize_first_letter(name):
    return name.capitalize()

def main():
    # Take a list of names as input from the user
    names = input("Enter a list of names separated by spaces: ").split()

    # Capitalize the first letter of each name
    capitalized_names = [capitalize_first_letter(name) for name in names]

    # Print each name as a separate list
    for name in capitalized_names:
        print([name])

if __name__ == "__main__":
    main()
def reverse_integer(num):
    # Convert the integer to a string and reverse it
    num_str = str(num)
    reversed_str = num_str[::-1]

    # Convert the reversed string back to an integer
    reversed_num = int(reversed_str)

    return reversed_num

def main():
    try:
        # Take the input integer from the user
        num = int(input("Enter an integer: "))

        # Reverse the integer and print the result
        reversed_num = reverse_integer(num)
        print("Reversed integer:", reversed_num)

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
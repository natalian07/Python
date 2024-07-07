def fibonacci_series(n):
    fib_series = [0, 1]

    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)

    return fib_series

def main():
    try:
        n = int(input("Enter the value of n: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return

        fib_series = fibonacci_series(n)
        print("Fibonacci Series up to the", n, "term:")
        print(fib_series)

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
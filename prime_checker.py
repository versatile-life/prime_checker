import sys

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 prime_checker.py <number>")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
    except ValueError:
        print("Please enter a valid integer.")
        sys.exit(1)

    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

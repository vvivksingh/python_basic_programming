def check_prime(n):
    prime = True
    for i in range(2, (int(n / 2) + 1)):
        if n % i == 0:
            prime = False
            break
    if prime:
        print(f"{n} is a prime number.")
    if not prime:
        print(f"{n} is a not a prime number.")


num = int(input("enter a number to check :"))

check_prime(num)

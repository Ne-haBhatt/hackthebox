def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = input()
numbers = list(map(int, n.split()))
prime_numbers = [num for num in numbers if is_prime(num)]
if len(prime_numbers) == 2:
    product = prime_numbers[0] * prime_numbers[1]
    print(product)
else:
    print("Not enough prime numbers in the list.")

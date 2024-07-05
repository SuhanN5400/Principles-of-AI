def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
        if is_prime:
            primes.append(num)
    return primes

n = 50
primes = generate_primes(n)
print("Prime numbers up to", n, ":", primes)

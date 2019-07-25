
def epi_generate_primes(n: int) -> list:
    if n < 2:
        return []
    size = (n - 3) // 2 + 1
    primes = [2]
    is_prime = [True] * size
    for i in range(size):
        if is_prime[i]:
            p = i * 2 + 3
            primes.append(p)
            for j in range(2 * i ** 2 + 6 * i + 3, size, p):
                is_prime[j] = False

    return primes

def my_generate_primes(n: int) -> list:
    primes = []
    for i in range(2, n + 1):
        is_prime = True
        for j in primes:
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    return primes
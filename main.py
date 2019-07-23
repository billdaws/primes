def check_equal(L1, L2):
    return len(L1) == len(L2) and sorted(L1) == sorted(L2)

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


if __name__ == '__main__':
    tests = [i for i in range(100000)]
    failed_tests = []
    for test in tests:
        l1 = epi_generate_primes(test)
        l2 = my_generate_primes(test)
        result = check_equal(l1, l2)
        if not result:
            failed_tests.append({
                "test": test,
                "epi": l1,
                "mine": l2
            })

    for failed in failed_tests:
        print("\ttest: ", failed["test"])
        print("\t epi: ", " ".join(str(x) for x in failed["epi"]))
        print("\tmine: ", " ".join(str(y) for y in failed["mine"]))
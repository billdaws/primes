def check_equal(L1, L2):
    return len(L1) == len(L2) and sorted(L1) == sorted(L2)

def compare_to_known(l, known):
    """Sort known before using this function.
    """
    return len(l) == len(known) and sorted(l) == known

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

def get_known():
    """Will only check first million primes.
    TODO get more
    """
    with open("data/primes1.txt") as f:
        content = f.readlines()
    content = sorted([int(x.strip()) for x in content])
    return content


if __name__ == '__main__':
    # TODO ugly
    num_tests = 10
    tests = [i for i in range(num_tests)]
    results = []
    known = get_known()
    for test in tests:
        epi = epi_generate_primes(test)
        mine = my_generate_primes(test)
        known_slice = [i for i in known if i <= test]
        epi_equals_known = compare_to_known(epi, known_slice)
        mine_equals_known = compare_to_known(mine, known_slice)
        results.append({
            "test": test,
            "result": check_equal(epi, mine) and mine_equals_known,
            "epi": epi,
            "mine": mine,
            "known": known_slice,
            "epi_equals_known": epi_equals_known,
            "mine_equals_known": mine_equals_known
        })

    for r in results:
        # tedious pretty printing
        print("\t             test: ", r["test"])
        print("\t           result: ", r["result"])
        print("\t              epi: ", " ".join(str(x) for x in r["epi"]))
        print("\t             mine: ", " ".join(str(y) for y in r["mine"]))
        print("\t            known: ", " ".join(str(k) for k in r["known"]))
        print("\t epi_equals_known: ", r["epi_equals_known"])
        print("\tmine_equals_known: ", r["mine_equals_known"])

    print("num tests: ", len(results))
    num_failed = len([r for r in results if not r["result"]])
    print("num failed: ", num_failed)
    print("pct failed tests: ", (num_failed / num_tests) * 100)
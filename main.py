from datetime import datetime
import export
import logging
import algorithms

logger = logging.getLogger(__name__)

def check_equal(L1, L2):
    return len(L1) == len(L2) and sorted(L1) == sorted(L2)

def compare_to_known(l, known):
    """Sort known before using this function.
    """
    return len(l) == len(known) and sorted(l) == known


def get_known():
    """Will only check first million primes.
    """
    with open("data/primes1.txt") as f:
        content = f.readlines()
    content = sorted([int(x.strip()) for x in content])
    return content


if __name__ == '__main__':
    results_file = "results/", datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    export.write_header(results_file)

    num_tests = 1000000
    num_failed = 0
    tests = [i for i in range(num_tests)]
    results = []
    known = get_known()
    for test in tests:
        print("test #", test)
        epi = algorithms.epi_generate_primes(test)
        mine = algorithms.my_generate_primes(test)
        known_slice = [i for i in known if i <= test]
        epi_equals_known = compare_to_known(epi, known_slice)
        mine_equals_known = compare_to_known(mine, known_slice)
        result = check_equal(epi, mine) and mine_equals_known
        results.append({
            "test": test,
            "result": result,
            "epi": epi,
            "mine": mine,
            "known": known_slice,
            "epi_equals_known": epi_equals_known,
            "mine_equals_known": mine_equals_known
        })
        if not result:
            num_failed += 1

    print("num tests: ", len(results))
    failed = [r for r in results if not r["result"]]
    num_failed = len(failed)
    print("num failed: ", num_failed)
    print("pct failed tests: ", (num_failed / num_tests) * 100)
from utils.get_input import getInputByCommaSeparator
from utils.math import factors

# Returns the accumulated sum of invalid IDs
def part1() -> int:
    id_range_list = getInputByCommaSeparator(2)
    addition = 0

    for id_range in id_range_list:
        start_str = id_range.split("-")[0]
        end_str = id_range.split("-")[1]

        start = int(start_str)
        end = int(end_str)

        for i in range(start, end+1):
            num_str = str(i)
            num_len = len(num_str)
            if num_len % 2 != 0:
                continue
            half_len = num_len // 2
            if num_str[:half_len] == num_str[half_len:]:
                addition += i

    return addition

# Returns the accumulated sum of invalid IDs
def part2() -> int:
    id_range_list = getInputByCommaSeparator(2)
    addition = 0

    for id_range in id_range_list:
        start_str = id_range.split("-")[0]
        end_str = id_range.split("-")[1]

        start = int(start_str)
        end = int(end_str)

        for i in range(start, end+1):
            num_str = str(i)
            matched = False

            if len(num_str) < 2:
                continue

            fac = factors(len(num_str))
            req_fac = fac[0:len(fac)-1]
            req_fac = req_fac[::-1]
            for j in req_fac:
                pattern = num_str[0:j]
                chunks = [num_str[i:i+j] for i in range(0, len(num_str), j)]
                matched = all(p == pattern for p in chunks)
                if matched:
                    addition += i
                    break


    return addition


if __name__ == "__main__":
    invalid_ids = part1()
    print("part1: " + str(invalid_ids))

    invalid_ids = part2()
    print("part2: " + str(invalid_ids))

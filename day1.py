from utils.get_input import getInputForDay

# Returns the password to open the door
def part1() -> int:
    lines = getInputForDay(1)
    current = 50
    password = 0

    for rotation in lines:
        dir = rotation[0]
        magnitude = int(rotation[1:])
        if dir == "L":
            magnitude = -magnitude

        current = (current + magnitude) % 100

        if current == 0:
            password += 1

    return password

# Returns the actual password to open the door
def part2() -> int:
    lines = getInputForDay(1)
    current = 50
    password = 0

    for rotation in lines:
        dir = rotation[0]
        magnitude = int(rotation[1:])
        if dir == "L":
            dist_to_zero = current if current > 0 else 100
            if magnitude >= dist_to_zero:
                password += 1
                remaining_mag = magnitude - dist_to_zero
                password += remaining_mag//100

            current = (current - magnitude) % 100
        else:
            password += (current + magnitude) // 100

            current = (current + magnitude) % 100

    return password


if __name__ == "__main__":
    password = part1()
    print("part1: " + str(password))

    password = part2()
    print("part2: " + str(password))

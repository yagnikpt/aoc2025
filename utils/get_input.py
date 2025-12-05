# returns the list of lines from the input file
def getInputForDay(day: int) -> list[str]:
    lines = []
    with open(f"inputs/day{day}.txt", "r") as f:
        for line in f:
            lines.append(line.strip())

    return lines

# returns the list of lines from the input file
def getInputByLines(day: int) -> list[str]:
    lines = []
    with open(f"inputs/day{day}.txt", "r") as f:
        for line in f:
            lines.append(line.strip())

    return lines

def getInputByCommaSeparator(day: int) -> list[str]:
    with open(f"inputs/day{day}.txt", "r") as f:
        content = f.read()
        parts = content.split(",")
        return parts

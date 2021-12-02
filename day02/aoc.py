from os import environ

def getSolutionPart1(data):
    h = 0
    d = 0
    for step in data:
        direction, x = step.split()
        x = int(x)
        if direction == 'forward':
            h += x
        elif direction == 'up':
            d -= x
        elif direction == 'down':
            d += x
    return h * d

def getSolutionPart2(data):
    h = 0
    d = 0
    aim = 0
    for step in data:
        direction, x = step.split()
        x = int(x)
        if direction == 'down':
            aim += x
        if direction == 'up':
            aim -= x
        if direction == 'forward':
            h += x
            d += aim * x
    return h * d

if __name__ == "__main__":
    data = open("input.txt").read().splitlines()
    part = environ.get('part')
    if part == 'part2':
        print(getSolutionPart2(data))
    else:
        print(getSolutionPart1(data))

from os import environ

def getSolutionPart1(data):
    gamma = ""
    epsilon = ""
    for i in range(len(data[0])):
        column = "".join(number[i] for number in data)
        if column.count("0") > column.count("1"):
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon
    
def getSolutionPart2(data):
    length = len(data[0])
    oxygen = set(data)
    co2 = set(data)

    # oxygen
    for i in range(length):
        column = "".join(number[i] for number in oxygen)
        if column.count("0") <= column.count("1"):
            bit = "1"
        else:
            bit = "0"

        oxygen = [number for number in oxygen if number[i] == bit]
        if len(oxygen) == 1:
            oxygen = int(oxygen[0], 2)
            break

    # co2
    for i in range(length):
        column = "".join(number[i] for number in co2)
        if column.count("0") > column.count("1"):
            bit = "1"
        else:
            bit = "0"

        co2 = [number for number in co2 if number[i] == bit]
        if len(co2) == 1:
            co2 = int(co2[0], 2)
            break
    return oxygen * co2


if __name__ == "__main__":
    inputFile = open('input.txt', 'r')
    data = [x.strip() for x in inputFile.readlines()]
    part = environ.get('part')
    if part == 'part2':
        print(getSolutionPart2(data))
    else:
        print(getSolutionPart1(data))

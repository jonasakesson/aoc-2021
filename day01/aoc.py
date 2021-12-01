from os import environ

def getSolutionPart1(data):
    count = 0        
    for i in range(1, len(data)):
        if data[i - 1] < data[i]:
            count += 1
    return count

def getSolutionPart2(data):      
    count = 0        
    for i in range(len(data) - 3):
        a = data[i] + data[i + 1] + data[i + 2]
        b = data[i + 1] + data[i + 2] + data[i + 3]
        if a < b:
            count += 1
    return count

if __name__ == "__main__":
    with open('input.txt') as f:
        data = [int(x) for x in f]
    #inputFile = open('input.txt', 'r')
    #data = [x.strip() for x in inputFile.readlines()]
    part = environ.get('part')
    if part == 'part2':
        print(getSolutionPart2(data))
    else:
        print(getSolutionPart1(data))

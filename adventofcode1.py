count = 0
previous = None
first = None
second = None
last = None
with open("./adventofcode.txt") as file:
    for line in file:
        line = line.rstrip()
        if first == None:
            first = int(line)
            continue
        elif second == None:
            second = int(line)
            continue
        elif last == None:
            last = int(line)
            if previous == None and first and second and last:
                previous = int(first) + int(second) + int(last)
                continue
        if previous and first and second and last:
            first = second
            second = last
            last = int(line)
            
            current = int(first) + int (second) + int(last)

            if current > previous:
                count += 1
            previous = int(current)

    print(count)
# #skipped day 4 temporarily. 6/12/22
# #part 1, maybe make every stack in a list?
# stacks = [['Q', 'H', 'C', 'T', 'N', 'S', 'V', 'B'], ['G', 'B', 'D', 'W'], ['B', 'Q', 'S', 'T', 'R', 'W', 'F'], ['N', 'D', 'J', 'Z', 'S', 'W', 'G', 'L'], ['F', 'V', 'D', 'P', 'M'] , ['J', 'W', 'F'], ['V', 'J', 'B', 'Q', 'N', 'L'], ['N', 'S', 'Q', 'J', 'C', 'R', 'T', 'G'], ['M', 'D', 'W', 'C', 'Q', 'S', 'J']
# ]


# def moveCrate(noOfCrates: int, stackMovedFrom: int, stackMovedTo: int):
#     stackToRemoveFrom = stacks[(stackMovedFrom - 1)]
#     del stackToRemoveFrom[2:stackMovedFrom]
#     stackToAddTo = stacks[(stackMovedTo - 1)]
#     stackToAddTo.extend(stackToRemoveFrom[0:noOfCrates])
#     # print(noOfCrates)
#     # print(stackMovedFrom)
#     # print(stackMovedTo)

# def printTopCrate():
#     print(stacks[0::9][0::9][0])

# with open("day5input.txt", 'r') as readfile:
#     for line in readfile.readlines()[10:]:
#         values = line.split()
#         x, y, z = int(values[1]), int(values[3]), int(values[5])
#         moveCrate(x, y, z)




# printTopCrate()
def parseQuery(query, grid):
    amount = int(query.split()[1])
    src = int(query.split()[3])-1
    dest = int(query.split()[5])-1

    for _ in range(amount):
        grid[dest] = [grid[src][0]] + grid[dest]
        grid[src].pop(0)

    return grid

with open('day5input.txt') as f:
    grid = [[], [], [], [], [], [], [], [], []]

    lines = f.readlines()

    for line in lines[:8]:
        i = 0
        for c in line[1::4]:
            if c.strip(): grid[i].append(c)
            i += 1

    for line in lines[10:]:
        if line.strip(): grid = parseQuery(line, grid)

    out = ""
    for row in grid: out += "".join(row[0])
    print(out)